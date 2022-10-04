"""recipes table added

Revision ID: 62d23f29fe51
Revises: b567f3d3c7dc
Create Date: 2022-10-04 22:54:11.437475

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import ForeignKey


# revision identifiers, used by Alembic.
revision = '62d23f29fe51'
down_revision = 'b567f3d3c7dc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('recipes',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipes_products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), ForeignKey('products.id')),
        sa.Column('recipe_id', sa.Integer(), ForeignKey('recipes.id')),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    pass
