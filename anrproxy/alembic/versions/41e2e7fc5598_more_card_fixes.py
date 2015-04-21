"""more card fixes

Revision ID: 41e2e7fc5598
Revises: 270a12c7527b
Create Date: 2015-04-20 23:34:10.367595

"""

# revision identifiers, used by Alembic.
revision = '41e2e7fc5598'
down_revision = '270a12c7527b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    card = sa.sql.table(
        'card', sa.sql.column('file_name'), sa.sql.column('card_name'))

    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('r-d-interface.png')).
        where(card.c.card_name == op.inline_literal('Archives Interface')).
        values(
            {'card_name': op.inline_literal('R&D Interface')})
        )
    op.bulk_insert(card, [
        {
            "file_name": "kate-mac-mccaffrey.png",
            "card_name": 'Kate "Mac" McCaffrey: Digital Tinkerer'
        }])


def downgrade():
    pass
