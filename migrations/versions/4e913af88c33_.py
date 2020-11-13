"""empty message

Revision ID: 4e913af88c33
Revises: 67216b6cf293
Create Date: 2020-09-18 15:04:03.359403

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from project import dbtypes


# revision identifiers, used by Alembic.
revision = '4e913af88c33'
down_revision = '67216b6cf293'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('analytics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.Unicode(length=255), nullable=True),
    sa.Column('value', sa.UnicodeText(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('analytics')
    # ### end Alembic commands ###
