"""Initial migration

Revision ID: c62bdb32461c
Revises: 
Create Date: 2025-03-08 23:03:03.000206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c62bdb32461c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'releases',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String(256), nullable=False),
        sa.Column('author', sa.String(256), nullable=False),
        sa.Column('type', sa.String(32), nullable=False),
        sa.Column('update_date', sa.DateTime, nullable=False),
    )

    op.create_table(
        'genres',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('genre', sa.String(32), nullable=False)
    )

    op.create_table(
        'releases_genres',
        sa.Column('release_id', sa.Integer, sa.ForeignKey('releases.id'), primary_key=True),
        sa.Column('genre_id', sa.Integer, sa.ForeignKey('genres.id'), primary_key=True)
    )

def downgrade():
    op.drop_table('releases')
    op.drop_table('genres')
    op.drop_table('releases_genres')