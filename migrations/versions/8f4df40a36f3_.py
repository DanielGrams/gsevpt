"""empty message

Revision ID: 8f4df40a36f3
Revises: f71c86333bfb
Create Date: 2020-09-24 18:53:02.861732

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from project import dbtypes


# revision identifiers, used by Alembic.
revision = "8f4df40a36f3"
down_revision = "f71c86333bfb"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "adminunitmemberinvitation",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("admin_unit_id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("roles", sa.UnicodeText(), nullable=True),
        sa.ForeignKeyConstraint(
            ["admin_unit_id"],
            ["adminunit.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email", "admin_unit_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("adminunitmemberinvitation")
    # ### end Alembic commands ###
