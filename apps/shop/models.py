import datetime

from apps.ext import db

class Shop(db.Model):
    shop_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    sub_title = db.Column(db.String(64))
    original_price = db.Column(db.Numeric(10, 2))
    promote_price = db.Column(db.Numeric(10, 2))
    stock = db.Column(db.Integer)
    cate_id = db.Column(db.Integer)
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
