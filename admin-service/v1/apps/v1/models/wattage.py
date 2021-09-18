from .db import db


class Wattage(db.Document):
    unit = db.StringField(required=True)
