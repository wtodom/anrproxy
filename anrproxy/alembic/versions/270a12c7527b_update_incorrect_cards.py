#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""update incorrect cards

Revision ID: 270a12c7527b
Revises: 25bc277cce91
Create Date: 2015-04-20 22:44:25.407411

"""

# revision identifiers, used by Alembic.
revision = '270a12c7527b'
down_revision = '25bc277cce91'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    card = sa.sql.table(
        'card', sa.sql.column('file_name'), sa.sql.column('card_name'))

    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('power-tap.png')).
        where(card.c.card_name == op.inline_literal('Power Nap')).
        values(
            {'card_name': op.inline_literal('Power Tap')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('quetzal.png')).
        where(card.c.card_name == op.inline_literal('Fetal AI')).
        values(
            {'card_name': op.inline_literal('Quetzal: Free Spirit')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('shi-kyu.png')).
        where(card.c.card_name == op.inline_literal('Ashigaru')).
        values(
            {'card_name': op.inline_literal('Shi.Kyū'.decode('utf-8'))})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('deus-ex.png')).
        where(card.c.card_name == op.inline_literal('Caduceus')).
        values(
            {'card_name': op.inline_literal('Deus Ex')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('mr-li.png')).
        where(card.c.card_name == op.inline_literal('Merlin')).
        values(
            {'card_name': op.inline_literal('Mr. Li')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('nasir-meidan.png')).
        where(card.c.card_name == op.inline_literal('Inside Man')).
        values(
            {'card_name': op.inline_literal('Nasir Meidan: Cyber Explorer')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('noise.png')).
        where(card.c.card_name == op.inline_literal('Diesel')).
        values(
            {'card_name': op.inline_literal('Noise: Hacker Extraordinaire')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('special-orde.png')).
        where(card.c.card_name == op.inline_literal('Special Order')).
        values(
            {'file_name': op.inline_literal('special-order.png')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('edward-kim.png')).
        where(card.c.card_name == op.inline_literal('Swarm')).
        values(
            {'card_name': op.inline_literal("Edward Kim: Humanity's Hammer")})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('weyland-consortium.png')).
        where(card.c.card_name == op.inline_literal(
            'Weyland Consortium: Because We Built It')).
        values(
            {'card_name': op.inline_literal(
                'Weyland Consortium: Building a Better World')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('tmi.jpg')).
        where(card.c.card_name == op.inline_literal('Inti')).
        values(
            {'card_name': op.inline_literal('TMI')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal(
            'rielle-kit-peddler-transhuman.jpg')).
        where(card.c.card_name == op.inline_literal(
            "Rielle 'Kit' Peddler: Transhuman")).
        values(
            {'card_name': op.inline_literal(
                'Rielle "Kit" Peddler: Transhuman')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('verberus-cujo-h3.jpg')).
        where(card.c.card_name == op.inline_literal("Cerberus 'Cuj.0' H3")).
        values(
            {'card_name': op.inline_literal('Cerberus "Cuj.0" H3'),
             'file_name': op.inline_literal('cerberus-cujo-h3.jpg')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('cerberus-lady-h1.jpg')).
        where(card.c.card_name == op.inline_literal("Cerberus 'Lady' H1")).
        values(
            {'card_name': op.inline_literal('Cerberus "Lady" H1')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('cerberus-rex-h2.jpg')).
        where(card.c.card_name == op.inline_literal("Cerberus 'Rex' H2")).
        values(
            {'card_name': op.inline_literal('Cerberus "Rex" H2')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal(
            'kate-mac-mccaffrey.png')).
        where(card.c.card_name == op.inline_literal(
            "Kate 'Mac' McCaffrey: Digital Tinker")).
        values({'card_name': op.inline_literal(
            'Kate "Mac" McCaffrey: Digital Tinker')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal(
            'ken-express-tenma-disappeared-clone.png')
        ).
        where(card.c.card_name == op.inline_literal(
            "Ken 'Express' Tenma: Disappeared Clone")
        ).
        values({'card_name': op.inline_literal(
            'Ken "Express" Tenma: Disappeared Clone')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('jinteki.jpg')).
        where(card.c.card_name == op.inline_literal('Inti')).
        values(
            {'card_name': op.inline_literal('Jinteki: Personal Evolution')})
        )
    op.execute(
        card.update().
        where(card.c.file_name == op.inline_literal('eak-efficiency.jpg')).
        where(card.c.card_name == op.inline_literal('Peak Efficiency')).
        values(
            {'file_name': op.inline_literal('peak-efficiency.jpg')})
        )


def downgrade():
    pass
