"""Creating billing.

Revision ID: 5669f7ffbd3
Revises: 2d7e457c5a1
Create Date: 2015-11-11 14:58:35.219182

"""

# revision identifiers, used by Alembic.
revision = '5669f7ffbd3'
down_revision = '2d7e457c5a1'
branch_labels = None
depends_on = None

from alembic import op
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String


def upgrade():
    op.create_table(
        'billings',
        Column(
            'id',
            Integer,
            primary_key=True
        ),
    )

    op.create_table(
        'bills',
        Column(
            'id',
            Integer,
            primary_key=True
        ),
        Column(
            'billing_id',
            Integer,
            ForeignKey('billings.id'),
        ),
        Column(
            'date',
            Date(),
            nullable=False,
        ),
        Column(
            'place',
            String,
        ),
    )


def downgrade():
    op.drop_table('bills')
    op.drop_table('billings')
