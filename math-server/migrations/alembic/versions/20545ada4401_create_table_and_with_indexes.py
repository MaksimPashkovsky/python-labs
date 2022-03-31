"""create table and with indexes

Revision ID: 20545ada4401
Revises: 
Create Date: 2022-03-21 15:44:31.257570

"""
from alembic import op
import sqlalchemy as sa
from operators import Operator


# revision identifiers, used by Alembic.
revision = '20545ada4401'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'history',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('operator', sa.Enum(Operator)),
        sa.Column('number1', sa.Numeric),
        sa.Column('number2', sa.Numeric),
        sa.Column('result', sa.Numeric),
        sa.Index('idx_operator', 'operator'),
        sa.Index('idx_result', 'result')
    )


def downgrade():
    op.drop_table('history')
    sa.Enum(Operator).drop(op.get_bind(), checkfirst=False)