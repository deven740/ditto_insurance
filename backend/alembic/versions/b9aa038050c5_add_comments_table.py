"""add comments table

Revision ID: b9aa038050c5
Revises: 901a9aa4004f
Create Date: 2024-07-03 18:23:41.912913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9aa038050c5'
down_revision: Union[str, None] = '901a9aa4004f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('policy_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['policy_id'], ['policies.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_id'), 'comments', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_id'), table_name='comments')
    op.drop_table('comments')
    # ### end Alembic commands ###
