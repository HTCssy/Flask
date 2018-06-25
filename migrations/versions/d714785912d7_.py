"""empty message

Revision ID: d714785912d7
Revises: 818d5b7762da
Create Date: 2018-06-21 09:48:09.680124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd714785912d7'
down_revision = '818d5b7762da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cate',
    sa.Column('cid', sa.Integer(), nullable=False),
    sa.Column('cname', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('cid')
    )
    op.create_index(op.f('ix_cate_cname'), 'cate', ['cname'], unique=True)
    op.create_table('user_6_20',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('weight', sa.Float(precision=10, asdecimal=2), nullable=True),
    sa.Column('money', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('msg', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_index(op.f('ix_user_6_20_name'), 'user_6_20', ['name'], unique=True)
    op.create_table('user_shop',
    sa.Column('sid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('cid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cid'], ['cate.cid'], ),
    sa.PrimaryKeyConstraint('sid')
    )
    op.create_index(op.f('ix_user_shop_name'), 'user_shop', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_shop_name'), table_name='user_shop')
    op.drop_table('user_shop')
    op.drop_index(op.f('ix_user_6_20_name'), table_name='user_6_20')
    op.drop_table('user_6_20')
    op.drop_index(op.f('ix_cate_cname'), table_name='cate')
    op.drop_table('cate')
    # ### end Alembic commands ###