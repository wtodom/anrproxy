from . import db


class Card(db.Model):
    file_name = db.Column(db.String(100), primary_key=True, nullable=False)
    card_name = db.Column(db.String(100), nullable=False)

    def __init__(self, file_name, card_name):
        self.file_name = file_name
        self.card_name = card_name
