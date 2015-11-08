"""empty message

Revision ID: 2d7e457c5a1
Revises:
Create Date: 2015-11-08 21:57:21.927065

"""

# revision identifiers, used by Alembic.
revision = '2d7e457c5a1'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


def upgrade():
    op.create_table(
        'users',
        Column(
            'id',
            Integer,
            primary_key=True
        ),
        Column(
            'name',
            String,
        ),
        Column(
            'email',
            String,
            unique=True,
        ),
        Column(
            'password',
            String(128),
        )
    )


def downgrade():
    op.drop_table('users')
