"""empty message

Revision ID: 975c22ae802b
Revises: 5c8457f2eac1
Create Date: 2020-07-17 11:27:53.084732

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from project import dbtypes


# revision identifiers, used by Alembic.
revision = '975c22ae802b'
down_revision = '5c8457f2eac1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eventorganizer',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=255), nullable=True),
    sa.Column('org_name', sa.Unicode(length=255), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('email', sa.Unicode(length=255), nullable=True),
    sa.Column('phone', sa.Unicode(length=255), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('event', sa.Column('organizer_id', sa.Integer(), nullable=True))
    op.alter_column('event', 'host_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('event', 'place_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'event', 'eventorganizer', ['organizer_id'], ['id'])
    op.drop_constraint('place_name_key', 'place', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('place_name_key', 'place', ['name'])
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.alter_column('event', 'place_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('event', 'host_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('event', 'organizer_id')
    op.drop_table('eventorganizer')
    # ### end Alembic commands ###
