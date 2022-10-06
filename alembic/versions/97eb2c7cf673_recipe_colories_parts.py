"""recipe colories parts

Revision ID: 97eb2c7cf673
Revises: 41b5efbaf5c0
Create Date: 2022-10-06 21:35:24.275015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97eb2c7cf673'
down_revision = '41b5efbaf5c0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('recipes',
        sa.Column('protein', sa.Float)
    )
    op.add_column('recipes',
        sa.Column('fats', sa.Float)
    )
    op.add_column('recipes',
        sa.Column('carbohydrates', sa.FLOAT)
    )


def downgrade() -> None:
    pass
