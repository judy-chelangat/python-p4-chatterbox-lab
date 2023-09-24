"""updated column createdat

Revision ID: 3322fdf5248f
Revises: 93f9a05486e8
Create Date: 2023-09-20 22:43:55.406432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3322fdf5248f'
down_revision = '93f9a05486e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.VARCHAR(),
               type_=sa.DateTime(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               existing_nullable=True)

    # ### end Alembic commands ###