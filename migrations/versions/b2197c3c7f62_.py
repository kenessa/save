"""empty message

Revision ID: b2197c3c7f62
Revises: 8d0ea9b72dbf
Create Date: 2017-10-10 15:35:35.990105

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b2197c3c7f62'
down_revision = '8d0ea9b72dbf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sg_drop_out', 'date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sg_drop_out', sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
