"""petimage deleted

Revision ID: 53984d4a0b17
Revises: 73914275fac8
Create Date: 2025-05-01 18:12:34.685584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53984d4a0b17'
down_revision = '73914275fac8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('interests', sa.String(length=200), nullable=True))
        batch_op.alter_column('pet_picture',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=256),
               existing_nullable=True)
        batch_op.drop_column('photo_url')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('photo_url', sa.VARCHAR(length=256), nullable=True))
        batch_op.alter_column('pet_picture',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=200),
               existing_nullable=True)
        batch_op.drop_column('interests')

    # ### end Alembic commands ###
