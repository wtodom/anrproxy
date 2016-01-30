"""pad campain was named adonis

Revision ID: 21f8c740d77d
Revises: 4d1e6fc4e9dd
Create Date: 2016-01-30 13:43:23.331721

"""

# revision identifiers, used by Alembic.
revision = '21f8c740d77d'
down_revision = '4d1e6fc4e9dd'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    card = sa.sql.table(
        'card', sa.sql.column('file_name'), sa.sql.column('card_name'))

    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('pad-campaign.png')).
        where(card.c.card_name == op.inline_literal('Adonis Campaign')).
        values(
            {'card_name': op.inline_literal('PAD Campaign')})
    )


def downgrade():
    pass
