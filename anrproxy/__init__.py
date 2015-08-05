#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import func

import yaml

import os
import re
import logging.config


here = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(here, 'logging.yaml'), 'r') as f:
    log_conf = yaml.load(f)
    log_conf['handlers']['info_file_handler']['filename'] = str(
        os.path.join(here, 'error.log'))
    log_conf['handlers']['error_file_handler']['filename'] = str(
        os.path.join(here, 'info.log'))

logger = logging.getLogger(__name__)

logging.config.dictConfig(log_conf)


app = Flask(__name__)
app.config.from_object('config')
toolbar = DebugToolbarExtension(app)

db = SQLAlchemy(app)


from .models import Card


def get_images(card_list):
    logger.info("Getting images.")
    card_files = []
    for card in card_list.split('\n'):
        if re.match('^([0-9])x ', card):
            card = card.strip()
            count = int(re.findall('^([0-9])x ', card)[0])
            name = re.findall('^[0-9]x (.*$)', card)[0]
            name = name.replace('\xe2\x80\xa2', '').strip()
            name = name.replace('•', '').strip()
            db_card = Card.query.filter(
                func.lower(name) == func.lower(Card.card_name)).first()
            if db_card:
                card_files.extend([db_card.file_name] * count)
            else:
                logger.error("Image not found for card: " + name.encode('utf-8'))
    return card_files


@app.route('/')
def index():
    placeholder = '\n'.join([
        'Format:',
        '3x Jackson Howard',
        '3x NAPD Contract',
        '3x Eli 1.0',
        'and so on...',
        '(netrunnerdb "plain text" also works)'])
    return render_template('index.html', placeholder=placeholder)


@app.route('/proxies', methods=['POST'])
def generate_proxies():
    print(request.form)
    cards = get_images(request.form['decklist'])
    return render_template(
        'proxies.html', cards=cards)


if __name__ == '__main__':
    app.run()
