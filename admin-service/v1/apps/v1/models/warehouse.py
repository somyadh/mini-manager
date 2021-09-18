from .db import db


class Warehouse(db.Document):
    name = db.StringField(required=True)
    address = db.StringField()
