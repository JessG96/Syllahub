"""create table CLO

Revision ID: 6e070ac5b5b8
Revises: b26218144c13
Create Date: 2019-03-22 00:45:41.156644

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6e070ac5b5b8'
down_revision = 'b26218144c13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'clo',
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('general', sa.String(length=256), nullable=True),
        sa.Column('specific', sa.String(length=256), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_table('clo')
    # ### end Alembic commands ###
