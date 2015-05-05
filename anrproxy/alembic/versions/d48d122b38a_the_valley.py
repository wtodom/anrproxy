"""the valley

Revision ID: d48d122b38a
Revises: 52df82fd60e5
Create Date: 2015-05-04 21:58:27.770886

"""

# revision identifiers, used by Alembic.
revision = 'd48d122b38a'
down_revision = '52df82fd60e5'
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
            "file_name": "adjusted-chronotype.png",
            "card_name": "Adjusted Chronotype"
        },
        {
            "file_name": "jinteki-biotech-the-tank.png",
            "card_name": "Jinteki Biotech: The Tank"
        },
        {
            "file_name": "bandwidth.png",
            "card_name": "Bandwidth"
        },
        {
            "file_name": "negotiator.png",
            "card_name": "Negotiator"
        },
        {
            "file_name": "brain-taping-warehouse.png",
            "card_name": "Brain-Taping Warehouse"
        },
        {
            "file_name": "next-gold.png",
            "card_name": "NEXT Gold"
        },
        {
            "file_name": "capital-investors.png",
            "card_name": "Capital Investors"
        },
        {
            "file_name": "paige-piper.png",
            "card_name": "Paige Piper"
        },
        {
            "file_name": "clot.png",
            "card_name": "Clot"
        },
        {
            "file_name": "predictive-algorithm.png",
            "card_name": "Predictive Algorithm"
        },
        {
            "file_name": "cortex-lock.png",
            "card_name": "Cortex Lock"
        },
        {
            "file_name": "spike.png",
            "card_name": "Spike"
        },
        {
            "file_name": "enhanced-vision.png",
            "card_name": "Enhanced Vision"
        },
        {
            "file_name": "symmetrical-visage.png",
            "card_name": "Symmetrical Visage"
        },
        {
            "file_name": "gene-conditioning-shoppe.png",
            "card_name": "Gene Conditioning Shoppe"
        },
        {
            "file_name": "synthetic-blood.png",
            "card_name": "Synthetic Blood"
        },
        {
            "file_name": "genetic-resequencing.png",
            "card_name": "Genetic Resequencing"
        },
        {
            "file_name": "tech-startup.png",
            "card_name": "Tech Startup"
        },
        {
            "file_name": "jinteki-biotech-life-imagined.png",
            "card_name": "Jinteki Biotech: Life Imagined"
        },
        {
            "file_name": "traffic-jam.png",
            "card_name": "Traffic Jam"
        },
        {
            "file_name": "jinteki-biotech-the-brewery.png",
            "card_name": "Jinteki Biotech: The Brewery"
        },
        {
            "file_name": "valley-grid.png",
            "card_name": "Valley Grid"
        },
        {
            "file_name": "jinteki-biotech-the-greenhouse.png",
            "card_name": "Jinteki Biotech: The Greenhouse"
        }
    ])


def downgrade():
    pass
