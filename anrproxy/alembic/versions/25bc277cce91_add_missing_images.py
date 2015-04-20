"""add missing images

Revision ID: 25bc277cce91
Revises: 14e9d429af5
Create Date: 2015-04-09 17:34:21.190181

"""

# revision identifiers, used by Alembic.
revision = '25bc277cce91'
down_revision = u'14e9d429af5'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    card = sa.sql.table('card', sa.sql.column('file_name'), sa.sql.column('card_name'))
    op.bulk_insert(card, [
        {"file_name": "andromeda.png", "card_name": "Andromeda: Dispossessed Ristie"},
        {"file_name": "weyland-argus-security.png", "card_name": "Argus Security: Protection Guaranteed"},
        {"file_name": "weyland-blue-sun.png", "card_name": "Blue Sun: Powering the Future"},
        {"file_name": "ash-2x3zb9cy.png", "card_name": "Ash 2X3ZB9CY"},
        {"file_name": "docklands-crackdown.png", "card_name": "Docklands Crackdown"},
        {"file_name": "fetal-ai.png", "card_name": "Fetal AI"},
        {"file_name": "grndl-refinery.png", "card_name": "GRNDL Refinery"},
        {"file_name": "gabriel-santiago.png", "card_name": "Gabriel Santiago: Consummate Professional"},
        {"file_name": "weyland-gagarin-deep-space.png", "card_name": "Gagarin Deep Space: Expanding the Horizon"},
        {"file_name": "haas-bioroid-etf.png", "card_name": "Haas-Bioroid: Engineering the Future"},
        {"file_name": "iq.png", "card_name": "IQ"},
        {"file_name": "jinteki-industrial-genomics.png", "card_name": "Industrial Genomics: Growing Solutions"},
        {"file_name": "leela-patel.png", "card_name": "Leela Patel: Trained Pragmatist"},
        {"file_name": "maxx.png", "card_name": "MaxX: Maximum Punk Rock"},
        {"file_name": "nbn-making-news.png", "card_name": "NBN: Making News"},
        {"file_name": "next-bronze.png", "card_name": "NEXT Bronze"},
        {"file_name": "next-silver.png", "card_name": "NEXT Silver"},
        {"file_name": "near-earth-hub.png", "card_name": "Near-Earth Hub: Broadcast Center"},
        {"file_name": "neural-emp.png", "card_name": "Neural EMP"},
        {"file_name": "nisei-mk-ii.png", "card_name": "Nisei MK II"},
        {"file_name": "plan-b.png", "card_name": "Plan B"},
        {"file_name": "rsvp.png", "card_name": "RSVP"},
        {"file_name": "tgtbt-true-colors.png", "card_name": "TGTBT"},
        {"file_name": "the-foundry.png", "card_name": "The Foundry: Refining the Process"},
        {"file_name": "weyland-titan-transnational.png", "card_name": "Titan Transnational: Investing In Your Future"},
        {"file_name": "valencia-estavez.png", "card_name": "Valencia Estevez: The Angel of Cayambe"},
        {"file_name": "whizzard-what-lies-ahead.png", "card_name": "Whizzard: Master Gamer"}
    ])


def downgrade():
    pass
