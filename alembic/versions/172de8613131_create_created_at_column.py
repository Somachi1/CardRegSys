"""create Created_at column

Revision ID: 172de8613131
Revises: 
Create Date: 2022-07-04 10:30:50.926518

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '172de8613131'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('visits', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass

def downgrade() -> None:
    op.drop_column('visits', 'created_at')
    pass
