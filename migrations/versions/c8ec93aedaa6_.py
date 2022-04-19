"""empty message

Revision ID: c8ec93aedaa6
Revises: 9ca81b8c01b0
Create Date: 2022-04-01 21:01:23.876340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8ec93aedaa6'
down_revision = '9ca81b8c01b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('save_keys', sa.Column('criador', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('save_keys', 'criador')
    # ### end Alembic commands ###