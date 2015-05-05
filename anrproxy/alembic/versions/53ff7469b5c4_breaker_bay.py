"""breaker bay

Revision ID: 53ff7469b5c4
Revises: d48d122b38a
Create Date: 2015-05-04 22:17:46.965212

"""

# revision identifiers, used by Alembic.
revision = '53ff7469b5c4'
down_revision = 'd48d122b38a'
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
            "file_name": "hacktivist-meeting.png",
            "card_name": "Hacktivist Meeting"
        },
        {
            "file_name": "off-campus-apartment.png",
            "card_name": "Off-Campus Apartment"
        },
        {
            "file_name": "career-fair.png",
            "card_name": "Career Fair"
        },
        {
            "file_name": "dorm-computer.png",
            "card_name": "Dorm Computer"
        },
        {
            "file_name": "hayley-kaplan.png",
            "card_name": "Hayley Kaplan: Universal Scholar"
        },
        {
            "file_name": "game-day.png",
            "card_name": "Game Day"
        },
        {
            "file_name": "comet.png",
            "card_name": "Comet"
        },
        {
            "file_name": "study-guide.png",
            "card_name": "Study Guide"
        },
        {
            "file_name": "london-library.png",
            "card_name": "London Library"
        },
        {
            "file_name": "tyson-observatory.png",
            "card_name": "Tyson Observatory"
        },
        {
            "file_name": "beach-party.png",
            "card_name": "Beach Party"
        },
        {
            "file_name": "research-grant.png",
            "card_name": "Research Grant"
        },
        {
            "file_name": "turing.png",
            "card_name": "Turing"
        },
        {
            "file_name": "crick.png",
            "card_name": "Crick"
        },
        {
            "file_name": "recruiting-trip.png",
            "card_name": "Recruiting Trip"
        },
        {
            "file_name": "blacklist.png",
            "card_name": "Blacklist"
        },
        {
            "file_name": "gutenberg.png",
            "card_name": "Gutenberg"
        },
        {
            "file_name": "student-loans.png",
            "card_name": "Student Loans"
        },
        {
            "file_name": "meru-mati.png",
            "card_name": "Meru Mati"
        },
        {
            "file_name": "breaker-bay-grid.png",
            "card_name": "Breaker Bay Grid"
        }
    ])


def downgrade():
    pass
