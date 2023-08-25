"""New Migration

Revision ID: baa9097006be
Revises: 
Create Date: 2023-01-01 18:24:48.148114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baa9097006be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_description'), 'event', ['description'], unique=False)
    op.create_index(op.f('ix_event_name'), 'event', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_event_name'), table_name='event')
    op.drop_index(op.f('ix_event_description'), table_name='event')
    op.drop_table('event')
    # ### end Alembic commands ###
