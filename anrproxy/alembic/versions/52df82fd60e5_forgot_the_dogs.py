"""forgot the dogs

Revision ID: 52df82fd60e5
Revises: 41e2e7fc5598
Create Date: 2015-04-20 23:50:43.223656

"""

# revision identifiers, used by Alembic.
revision = '52df82fd60e5'
down_revision = '41e2e7fc5598'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    card = sa.sql.table(
        'card', sa.sql.column('file_name'), sa.sql.column('card_name'))

    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('cerberus-lady-h1.png')).
        where(card.c.card_name == op.inline_literal("Cerberus 'Lady' H1")).
        values(
            {'card_name': op.inline_literal('Cerberus "Lady" H1')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('cerberus-rex-h2.png')).
        where(card.c.card_name == op.inline_literal("Cerberus 'Rex' H2")).
        values(
            {'card_name': op.inline_literal('Cerberus "Rex" H2')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('verberus-cujo-h3.png')).
        where(card.c.card_name == op.inline_literal("Cerberus 'Cuj.0' H3")).
        values(
            {'card_name': op.inline_literal('Cerberus "Cuj.0" H3'),
             'file_name': op.inline_literal('cerberus-cujo-h3.png')})
        )


def downgrade():
    pass
