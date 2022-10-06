"""recipe colories

Revision ID: 41b5efbaf5c0
Revises: 62d23f29fe51
Create Date: 2022-10-06 21:27:54.737663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41b5efbaf5c0'
down_revision = '62d23f29fe51'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('recipes',
        sa.Column('calories', sa.Float)
    )


def downgrade() -> None:
    pass
