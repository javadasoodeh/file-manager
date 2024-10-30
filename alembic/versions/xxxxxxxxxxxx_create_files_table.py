# alembic/versions/xxxxxxxxxxxx_create_files_table.py
"""Create files table

Revision ID: xxxxxxxxxxxx
Revises:
Create Date: YYYY-MM-DD HH:MM:SS

"""
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'xxxxxxxxxxxx'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'files',
        sa.Column('file_id', sa.String(length=36), primary_key=True, index=True),
        sa.Column('name_main', sa.String(length=255), nullable=False),
        sa.Column('content_type', sa.String(length=100), nullable=False),
        sa.Column('size', sa.Integer(), nullable=False),
        sa.Column('extension', sa.String(length=10), nullable=False),
    )


def downgrade():
    op.drop_table('files')
