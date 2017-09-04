"""empty message

Revision ID: 19641592eaf9
Revises: 45e86735e146
Create Date: 2017-09-04 11:37:25.324666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19641592eaf9'
down_revision = '45e86735e146'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sg_member', sa.Column('pin', sa.String(length=4), nullable=True))
    op.create_index(op.f('ix_sg_member_pin'), 'sg_member', ['pin'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_sg_member_pin'), table_name='sg_member')
    op.drop_column('sg_member', 'pin')
    # ### end Alembic commands ###
