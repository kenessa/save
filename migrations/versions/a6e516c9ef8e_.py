"""empty message

Revision ID: a6e516c9ef8e
Revises: ac165c3d263c
Create Date: 2017-08-15 15:22:30.301639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6e516c9ef8e'
down_revision = 'ac165c3d263c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'user_fin_details_user_id_fkey', 'user_fin_details', type_='foreignkey')
    op.create_foreign_key(None, 'user_fin_details', 'users', ['user_id'], ['id'])
    op.add_column('users', sa.Column('confirmation_code', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('first_login', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'first_login')
    op.drop_column('users', 'confirmation_code')
    op.drop_constraint(None, 'user_fin_details', type_='foreignkey')
    op.create_foreign_key(u'user_fin_details_user_id_fkey', 'user_fin_details', 'organization', ['user_id'], ['id'])
    # ### end Alembic commands ###
