"""initial migrations 2

Revision ID: 72046cc63d10
Revises: 
Create Date: 2024-12-23 18:46:03.126561

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '72046cc63d10'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('coefficient', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.Integer(), nullable=True),
    sa.Column('status', sa.Enum('PENDING', 'TEAM_1_WINS', 'TEAM_2_WINS', name='status'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    # ### end Alembic commands ###
