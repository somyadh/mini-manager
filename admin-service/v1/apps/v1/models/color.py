from .db import db
from ..utils.constants.colors import Color


class Color(db.Document):
    a = Color()
    name = db.StringField(required=True, choices=a.availableColorList(), unique=True)