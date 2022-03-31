"""create composite index

Revision ID: f3087bfa3564
Revises: 20545ada4401
Create Date: 2022-03-21 15:47:38.627779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3087bfa3564'
down_revision = '20545ada4401'
branch_labels = None
depends_on = None


def upgrade():
    op.create_index('idx_op_n1_n2', 'history', ['operator', 'number1', 'number2'])


def downgrade():
    op.drop_index('idx_op_n1_n2', 'history')
