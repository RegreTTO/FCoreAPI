"""logo_link

Revision ID: 82eed59237a1
Revises: 90851146add4
Create Date: 2022-10-15 13:34:55.990691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82eed59237a1'
down_revision = '90851146add4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('recipes',
        sa.Column('logo_link', sa.String())
    )


def downgrade() -> None:
    pass
