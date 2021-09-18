from .db import db


class Vendor(db.Document):
    name = db.StringField(required=True)
    address = db.StringField()