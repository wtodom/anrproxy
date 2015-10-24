"""fix kate's card name

Revision ID: 63a12b04267
Revises: 3afec8fb951b
Create Date: 2015-10-23 18:16:34.993369

"""

# revision identifiers, used by Alembic.
revision = '63a12b04267'
down_revision = '3afec8fb951b'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    card = sa.sql.table(
        'card', sa.sql.column('file_name'), sa.sql.column('card_name'))

    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('kate-mac-mccaffrey.png')).
        where(card.c.card_name == op.inline_literal('Kate "Mac" McCaffrey: Digital Tinkerer')).
        values(
            {'card_name': op.inline_literal('Kate "Mac" McCaffrey: Digital Tinker')})
    )


def downgrade():
    pass
