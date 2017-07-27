"""empty message

Revision ID: 718e36d598de
Revises: 84b81dbc95df
Create Date: 2016-08-14 15:00:54.847069

"""

# revision identifiers, used by Alembic.
revision = '718e36d598de'
down_revision = '84b81dbc95df'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('panel_permissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('panel_name', sa.String(), nullable=True),
    sa.Column('role_name', sa.String(), nullable=True),
    sa.Column('can_access', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('panel_permissions')
    ### end Alembic commands ###