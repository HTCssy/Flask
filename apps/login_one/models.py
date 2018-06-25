from apps.ext import db
from flask_login import UserMixin

class UserLogin(db.Model, UserMixin):
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(64), nullable=False)


    #如果使用自定义的id需要重写该方法
    def get_id(self):
        return self.uid