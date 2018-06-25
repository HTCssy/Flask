#模块层
from apps.ext import db


class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    create_date = db.Column(db.DateTime)
    status = db.Column(db.Boolean)
    desc = db.Column(db.Text)