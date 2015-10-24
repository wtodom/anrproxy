"""fix deux x card_name

Revision ID: 571d3a87984b
Revises: 51535c1baed9
Create Date: 2015-10-23 19:27:32.061327

"""

# revision identifiers, used by Alembic.
revision = '571d3a87984b'
down_revision = '51535c1baed9'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    card = sa.sql.table(
        'card', sa.sql.column('file_name'), sa.sql.column('card_name'))

    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('deus-x.png')).
        where(card.c.card_name == op.inline_literal('Caduceus')).
        values(
            {'card_name': op.inline_literal('Deus X')})
    )


def downgrade():
    pass
