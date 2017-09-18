"""empty message

Revision ID: 99d5cb2ed427
Revises: 16c1ce0a496e
Create Date: 2017-09-18 17:27:36.110137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99d5cb2ed427'
down_revision = '16c1ce0a496e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member_approved_social', sa.Column('sg_member_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_member_approved_social_sg_member_id'), 'member_approved_social', ['sg_member_id'], unique=False)
    op.drop_index('ix_member_approved_social_committee_id', table_name='member_approved_social')
    op.drop_constraint(u'member_approved_social_committee_id_fkey', 'member_approved_social', type_='foreignkey')
    op.create_foreign_key(None, 'member_approved_social', 'sg_member', ['sg_member_id'], ['id'])
    op.drop_column('member_approved_social', 'committee_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member_approved_social', sa.Column('committee_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'member_approved_social', type_='foreignkey')
    op.create_foreign_key(u'member_approved_social_committee_id_fkey', 'member_approved_social', 'sg_member', ['committee_id'], ['id'])
    op.create_index('ix_member_approved_social_committee_id', 'member_approved_social', ['committee_id'], unique=False)
    op.drop_index(op.f('ix_member_approved_social_sg_member_id'), table_name='member_approved_social')
    op.drop_column('member_approved_social', 'sg_member_id')
    # ### end Alembic commands ###
