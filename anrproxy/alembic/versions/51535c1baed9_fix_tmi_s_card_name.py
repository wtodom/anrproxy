"""fix TMI's card_name

Revision ID: 51535c1baed9
Revises: 63a12b04267
Create Date: 2015-10-23 19:21:35.098667

"""

# revision identifiers, used by Alembic.
revision = '51535c1baed9'
down_revision = '63a12b04267'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    card = sa.sql.table(
        'card', sa.sql.column('file_name'), sa.sql.column('card_name'))

    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('tmi.png')).
        where(card.c.card_name == op.inline_literal('Inti')).
        values(
            {'card_name': op.inline_literal('TMI')})
    )


def downgrade():
    pass
