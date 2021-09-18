from .db import db


class Company(db.Document):
    name = db.StringField(required=True, unique=True)
