"""Initial Migration

Revision ID: 6f40498742cd
Revises: 379aeee5b341
Create Date: 2024-09-26 13:25:51.769235

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6f40498742cd'
down_revision = '379aeee5b341'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('code', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('description', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('image', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('quantity', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('inventoryStatus', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('rating', sa.Integer(), nullable=False))
        batch_op.drop_column('status')
        batch_op.drop_column('review')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('review', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('status', mysql.VARCHAR(length=80), nullable=False))
        batch_op.drop_column('rating')
        batch_op.drop_column('inventoryStatus')
        batch_op.drop_column('quantity')
        batch_op.drop_column('image')
        batch_op.drop_column('description')
        batch_op.drop_column('code')

    # ### end Alembic commands ###
