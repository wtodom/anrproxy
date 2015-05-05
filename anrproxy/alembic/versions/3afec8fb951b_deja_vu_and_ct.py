#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""deja vu and CT

Revision ID: 3afec8fb951b
Revises: 53ff7469b5c4
Create Date: 2015-05-04 22:41:13.583960

"""

# revision identifiers, used by Alembic.
revision = '3afec8fb951b'
down_revision = '53ff7469b5c4'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    card = sa.sql.table(
        'card',
        sa.sql.column('file_name'),
        sa.sql.column('card_name'))

    op.bulk_insert(card, [
        {
            "file_name": "deja-vu.png",
            "card_name": "Déjà Vu".decode('utf-8')
        },
        {
            "file_name": "chaos-theory.png",
            "card_name": "Chaos Theory: Wünderkind".decode('utf-8')
        }
    ])


def downgrade():
    pass
