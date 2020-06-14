"""empty message

Revision ID: a2ba246b23d0
Revises: 36945eb387b4
Create Date: 2020-06-14 19:39:43.809236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2ba246b23d0'
down_revision = '36945eb387b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('adminunit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('adminunitmemberrole',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('permissions', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('adminunitorgrole',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('permissions', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('orgmemberrole',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('permissions', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('adminunitmember',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin_unit_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['admin_unit_id'], ['adminunit.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('adminunitorg',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin_unit_id', sa.Integer(), nullable=False),
    sa.Column('organization_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['admin_unit_id'], ['adminunit.id'], ),
    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin_unit_id', sa.Integer(), nullable=False),
    sa.Column('host', sa.Unicode(length=255), nullable=False),
    sa.Column('external_link', sa.String(length=255), nullable=True),
    sa.Column('location', sa.Unicode(length=255), nullable=False),
    sa.Column('name', sa.Unicode(length=255), nullable=False),
    sa.Column('description', sa.UnicodeText(), nullable=False),
    sa.Column('verified', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['admin_unit_id'], ['adminunit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orgmember',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('organization_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('adminunitmemberroles_members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['adminunitmember.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['adminunitmemberrole.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('adminunitorgroles_organizations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('admin_unit_org_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_unit_org_id'], ['adminunitorg.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['adminunitorgrole.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('eventdate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.Column('start', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orgmemberroles_members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['member_id'], ['orgmember.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['orgmemberrole.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orgmemberroles_members')
    op.drop_table('eventdate')
    op.drop_table('adminunitorgroles_organizations')
    op.drop_table('adminunitmemberroles_members')
    op.drop_table('orgmember')
    op.drop_table('event')
    op.drop_table('adminunitorg')
    op.drop_table('adminunitmember')
    op.drop_table('orgmemberrole')
    op.drop_table('organization')
    op.drop_table('adminunitorgrole')
    op.drop_table('adminunitmemberrole')
    op.drop_table('adminunit')
    # ### end Alembic commands ###
