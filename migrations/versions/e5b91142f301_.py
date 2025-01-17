"""empty message

Revision ID: e5b91142f301
Revises: 333bb854aaf5
Create Date: 2021-05-21 10:38:35.418376

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5b91142f301'
down_revision = '333bb854aaf5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video', 'available_inventory')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('available_inventory', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
