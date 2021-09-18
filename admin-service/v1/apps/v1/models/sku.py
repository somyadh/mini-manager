from .db import db
from .wattage import Wattage
from .color import Color
from .company import Company


class SKU(db.Document):
    name = db.StringField(required=True)
    pc_per_box = db.IntField()
    box_qty = db.IntField()
    loose_pc_qty = db.IntField()
    wattage = db.ReferenceField(Wattage)
    color = db.ReferenceField(Color)
    company = db.ReferenceField(Company)
