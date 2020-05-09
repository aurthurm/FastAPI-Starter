"""empty message

Revision ID: a79a697b53ad
Revises: cce0a38ed48b
Create Date: 2020-04-09 14:40:36.820100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a79a697b53ad'
down_revision = 'cce0a38ed48b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('digitalcontent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('automatic_fulfillment', sa.Boolean(), nullable=True),
    sa.Column('content_file', sa.LargeBinary(), nullable=True),
    sa.Column('max_downloads', sa.Integer(), nullable=True),
    sa.Column('url_valid_days', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('variantimage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('productimage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('image', sa.LargeBinary(), nullable=True),
    sa.Column('alt', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('productvariant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sku', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('price_override_amount', sa.Float(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('track_inventory', sa.Boolean(), nullable=True),
    sa.Column('old_price', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('productvariant')
    op.drop_table('productimage')
    op.drop_table('variantimage')
    op.drop_table('digitalcontent')
    # ### end Alembic commands ###