"""Initial migration

Revision ID: 3911146fabc1
Revises: c23081b5b23a
Create Date: 2024-04-18 20:02:34.283218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3911146fabc1'
down_revision: Union[str, None] = 'c23081b5b23a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
