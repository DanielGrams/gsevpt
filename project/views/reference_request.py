from flask import flash, redirect, render_template, url_for
from flask_babelex import gettext
from flask_security import auth_required
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import desc

from project import app, db
from project.access import (
    access_or_401,
    get_admin_unit_for_manage_or_404,
    get_admin_units_for_event_reference_request,
    has_admin_unit_member_permission,
)
from project.forms.reference_request import CreateEventReferenceRequestForm
from project.models import (
    AdminUnitMember,
    Event,
    EventReferenceRequest,
    EventReferenceRequestReviewStatus,
    User,
)
from project.services.reference import get_reference_requests_incoming_query
from project.views.utils import (
    flash_errors,
    get_pagination_urls,
    handleSqlError,
    send_mail,
)


@app.route("/manage/admin_unit/<int:id>/reference_requests/incoming")
@auth_required()
def manage_admin_unit_reference_requests_incoming(id):
    admin_unit = get_admin_unit_for_manage_or_404(id)
    requests = (
        get_reference_requests_incoming_query(admin_unit)
        .order_by(desc(EventReferenceRequest.created_at))
        .paginate()
    )

    return render_template(
        "manage/reference_requests_incoming.html",
        admin_unit=admin_unit,
        requests=requests.items,
        pagination=get_pagination_urls(requests, id=id),
    )


@app.route("/manage/admin_unit/<int:id>/reference_requests/outgoing")
@auth_required()
def manage_admin_unit_reference_requests_outgoing(id):
    admin_unit = get_admin_unit_for_manage_or_404(id)
    requests = (
        EventReferenceRequest.query.join(Event)
        .filter(Event.admin_unit_id == admin_unit.id)
        .order_by(desc(EventReferenceRequest.created_at))
        .paginate()
    )

    return render_template(
        "manage/reference_requests_outgoing.html",
        admin_unit=admin_unit,
        requests=requests.items,
        pagination=get_pagination_urls(requests, id=id),
    )


@app.route("/event/<int:event_id>/reference_request/create", methods=("GET", "POST"))
@auth_required()
def event_reference_request_create(event_id):
    event = Event.query.get_or_404(event_id)
    access_or_401(event.admin_unit, "reference_request:create")

    form = CreateEventReferenceRequestForm()
    form.admin_unit_id.choices = sorted(
        [
            (admin_unit.id, admin_unit.name)
            for admin_unit in get_admin_units_for_event_reference_request(event)
        ],
        key=lambda admin_unit: admin_unit[1],
    )

    if form.validate_on_submit():
        request = EventReferenceRequest()
        request.review_status = EventReferenceRequestReviewStatus.inbox
        form.populate_obj(request)
        request.event = event

        try:
            db.session.add(request)
            db.session.commit()
            send_reference_request_inbox_mails(request)
            flash(
                gettext(
                    "Request successfully created. You will be notified after the other organization reviews the event."
                ),
                "success",
            )
            return redirect(
                url_for(
                    "manage_admin_unit_reference_requests_outgoing",
                    id=event.admin_unit_id,
                )
            )
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(handleSqlError(e), "danger")
    else:
        flash_errors(form)

    return render_template("event/reference_request.html", form=form, event=event)


def send_reference_request_inbox_mails(request):
    # Benachrichtige alle Mitglieder der AdminUnit, die diesen Request verifizieren können
    members = (
        AdminUnitMember.query.join(User)
        .filter(AdminUnitMember.admin_unit_id == request.admin_unit_id)
        .all()
    )

    for member in members:
        if has_admin_unit_member_permission(member, "reference_request:verify"):
            send_mail(
                member.user.email,
                gettext("New reference request"),
                "reference_request_notice",
                request=request,
            )
