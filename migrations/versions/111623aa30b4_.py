"""empty message

Revision ID: 111623aa30b4
Revises: a1544ec76c1d
Create Date: 2025-07-07 03:00:18.688278

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '111623aa30b4'
down_revision = 'a1544ec76c1d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('banner_url', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('role', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('location', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('bio', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('bio')
        batch_op.drop_column('location')
        batch_op.drop_column('role')
        batch_op.drop_column('banner_url')

    # ### end Alembic commands ###
