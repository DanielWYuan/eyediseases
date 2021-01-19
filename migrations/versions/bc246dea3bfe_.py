"""empty message

Revision ID: bc246dea3bfe
Revises: d14bd11bdd0d
Create Date: 2020-06-28 21:08:50.099833

"""
#  Copyright (c) 2018-2021 Beijing Ekitech Co., Ltd.
#  All rights reserved.

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bc246dea3bfe'
down_revision = 'd14bd11bdd0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('epigenetic_alteration',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('gene', sa.String(length=128), nullable=True),
    sa.Column('normal_retina', sa.Float(), nullable=True),
    sa.Column('amd_retina', sa.Float(), nullable=True),
    sa.Column('normal_rpe', sa.Float(), nullable=True),
    sa.Column('amd_rpe', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_epigenetic_alteration_gene'), 'epigenetic_alteration', ['gene'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_epigenetic_alteration_gene'), table_name='epigenetic_alteration')
    op.drop_table('epigenetic_alteration')
    # ### end Alembic commands ###