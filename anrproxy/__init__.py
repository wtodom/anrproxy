#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.sqlalchemy import SQLAlchemy

import re


app = Flask(__name__)
app.config.from_object('config')
toolbar = DebugToolbarExtension(app)

db = SQLAlchemy(app)


from .models import Card


def get_images(card_list):
    card_files = []
    for card in card_list.split('\n'):
        if re.match('^([0-9])x ', card):
            card = card.strip()
            count = int(re.findall('^([0-9])x ', card)[0])
            name = re.findall('^[0-9]x (.*$)', card)[0]
            name = name.replace('\xe2\x80\xa2', '').strip()
            name = name.replace('•', '').strip()
            db_card = Card.query.filter_by(card_name=name).first()
            # print(db_card)
            if db_card:
                card_files.extend([db_card.file_name] * count)
            else:
                # log somehow
                pass
    return card_files


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/proxies', methods=['POST'])
def generate_proxies():
    print(request.form)
    cards = get_images(request.form['decklist'])
    # print(cards)
    return render_template('proxies.html', cards=cards)


if __name__ == '__main__':
    app.run()
