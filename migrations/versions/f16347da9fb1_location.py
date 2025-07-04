"""location

Revision ID: f16347da9fb1
Revises: 53984d4a0b17
Create Date: 2025-05-01 19:05:21.276640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f16347da9fb1'
down_revision = '53984d4a0b17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pets', schema=None) as batch_op:
        batch_op.drop_column('location')

    # ### end Alembic commands ###
