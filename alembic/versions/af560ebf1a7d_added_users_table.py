"""Added users table

Revision ID: af560ebf1a7d
Revises: 
Create Date: 2026-02-08 21:14:45.945008

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af560ebf1a7d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users',
        sa.Column('id', sa.Integer(), autoincrement=True),
        sa.Column('username', sa.String(50), nullable=False, unique=True),
        sa.Column('fullname', sa.String(50), nullable=False, unique=True),
        sa.Column('email', sa.String(50), nullable=False, unique=True),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('role', sa.Enum('admin', 'siswa', 'guru', name='role'), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP, nullable=False),
        sa.Column('updated_at', sa.TIMESTAMP, nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
