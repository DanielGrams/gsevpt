from sqlalchemy.sql import and_, func

from project import db
from project.models import EventPlace, Location


def get_event_place(admin_unit_id, name):
    return EventPlace.query.filter(
        and_(
            EventPlace.name == name,
            EventPlace.admin_unit_id == admin_unit_id,
        )
    ).first()


def upsert_event_place(admin_unit_id, name):
    result = get_event_place(admin_unit_id, name)
    if result is None:
        result = EventPlace(name=name, admin_unit_id=admin_unit_id)
        result.location = Location()
        db.session.add(result)

    return result


def get_event_places(admin_unit_id):
    return (
        EventPlace.query.filter(EventPlace.admin_unit_id == admin_unit_id)
        .order_by(func.lower(EventPlace.name))
        .all()
    )
