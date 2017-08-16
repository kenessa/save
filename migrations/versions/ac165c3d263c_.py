"""empty message

Revision ID: ac165c3d263c
Revises: 2fb973ea5b6a
Create Date: 2017-08-14 17:11:03.276419

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac165c3d263c'
down_revision = '2fb973ea5b6a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_fin_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('type', sa.Integer(), nullable=True),
    sa.Column('account', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['organization.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_fin_details_user_id'), 'user_fin_details', ['user_id'], unique=False)
    op.add_column(u'users', sa.Column('birth_date', sa.Date(), nullable=True))
    op.add_column(u'users', sa.Column('education', sa.String(length=64), nullable=True))
    op.add_column(u'users', sa.Column('gender', sa.Integer(), nullable=True))
    op.add_column(u'users', sa.Column('location', sa.String(length=128), nullable=True))
    op.add_column(u'users', sa.Column('secondary_phone', sa.String(length=30), nullable=True))
    op.create_unique_constraint(None, 'users', ['secondary_phone'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column(u'users', 'secondary_phone')
    op.drop_column(u'users', 'location')
    op.drop_column(u'users', 'gender')
    op.drop_column(u'users', 'education')
    op.drop_column(u'users', 'birth_date')
    op.drop_index(op.f('ix_user_fin_details_user_id'), table_name='user_fin_details')
    op.drop_table('user_fin_details')
    # ### end Alembic commands ###
