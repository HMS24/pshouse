"""empty message

Revision ID: 8789035fea99
Revises: 
Create Date: 2022-08-15 16:01:19.643298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8789035fea99'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deals',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('city', sa.String(length=3), nullable=False),
    sa.Column('district', sa.String(length=8), nullable=False),
    sa.Column('object_of_transaction', sa.String(length=16), nullable=False),
    sa.Column('location', sa.String(length=128), nullable=False),
    sa.Column('transaction_date', sa.DATE(), nullable=False),
    sa.Column('level', sa.String(length=8), nullable=False),
    sa.Column('total_floor_numbers', sa.String(length=2), nullable=False),
    sa.Column('building_state', sa.String(length=16), nullable=False),
    sa.Column('main_use', sa.String(length=16), nullable=False),
    sa.Column('land_total_area', sa.Float(), nullable=False),
    sa.Column('building_total_area', sa.Float(), nullable=False),
    sa.Column('room', sa.String(length=1), nullable=False),
    sa.Column('restaurant_and_living_room', sa.String(length=1), nullable=False),
    sa.Column('bathroom', sa.String(length=1), nullable=False),
    sa.Column('build_name', sa.String(length=32), nullable=False),
    sa.Column('buildings', sa.String(length=32), nullable=False),
    sa.Column('parking_sapce_type', sa.String(length=8), nullable=False),
    sa.Column('parking_sapce_total_area', sa.Float(), nullable=False),
    sa.Column('parking_sapce_price', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Integer(), nullable=False),
    sa.Column('note', sa.String(length=128), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_deals_build_name'), 'deals', ['build_name'], unique=False)
    op.create_index(op.f('ix_deals_city'), 'deals', ['city'], unique=False)
    op.create_index(op.f('ix_deals_district'), 'deals', ['district'], unique=False)
    op.create_index(op.f('ix_deals_transaction_date'), 'deals', ['transaction_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_deals_transaction_date'), table_name='deals')
    op.drop_index(op.f('ix_deals_district'), table_name='deals')
    op.drop_index(op.f('ix_deals_city'), table_name='deals')
    op.drop_index(op.f('ix_deals_build_name'), table_name='deals')
    op.drop_table('deals')
    # ### end Alembic commands ###
