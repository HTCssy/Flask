import datetime

from apps.ext import db

'''
约束
    主键约束 唯一约束 非空约束 默认约束
    外键约束 关联关系
'''
'''
常用的数据类型
    数字相关
    字符串
    日期时间
    大文本  二进制数据
'''

class User_6_20(db.Model):
    #重命名
    # __tablename__ = 't_user'
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True, nullable=True)
    weight = db.Column(db.Float(10, 2))
    #相当于decimal
    money = db.Column(db.Numeric(10, 2))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now())
    #不要在text字段上加索引
    msg = db.Column(db.Text())

#外键,一对多
#1.在主表建立外键连接的关系
#2.在子表建立外键
class Cate(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(64), index=True, unique=True)
    #建立关联关系的对象,懒加载
    '''
     参数一  argument 关联对象的类名
     参数二  lazy 
            可选项:
            1.select 默认值 一条sql语句把所有的相关的数据全部查出来 
            2.dynamic 只查询主表的数据,生成查询子表的sql语句,需要子表的数据时再去查询
            3.immediate  等主表数据查询完成之后再去查询子表的数据
     参数 可选项      
        uselist=None, 建立一对一关系  uselist = False
        order_by=False, 排序时候使用order_by = [UserShop.sid]
        backref=None,反向引用(当两个对象需要双向引用时候使用)
        back_populates=None,
    '''
    shops = db.relationship('UserShop', back_populates='cate', lazy='dynamic')
#子表
class UserShop(db.Model):
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    #类名小写.关联子段,只是单纯的建立一个外键关系
    cid = db.Column(db.Integer, db.ForeignKey('cate.cid'))
    #同上
    # cid = db.Column(db.Integer, db.ForeignKey(Cate.cid))
    #双向引用时候使用
    cate = db.relationship('Cate', back_populates='shops')
    #一对一
    detail = db.relationship('Detail', uselist=False,backref='usershop' )

class Detail(db.Model):
    did = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Numeric(10, 2))
    sid = db.Column(db.Integer, db.ForeignKey(UserShop.sid))


#####################
#多对多
'''
定义多对多的第三张表
参数  表的名称
'''
relation = db.Table('role_Permission_relation',
         db.Column('id', db.Integer, primary_key=True),
         db.Column('per_id', db.Integer, db.ForeignKey('permission.per_id')),
         db.Column('role_id', db.Integer, db.ForeignKey('role.role_id'))
         )
#角色  secondary用于指向第三张表
class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    desc = db.Column(db.Text)
    permission = db.relationship('Permission', secondary=relation)
    def __init__(self, role_name, desc):
        self.role_name = role_name
        self.desc = desc

#权限
class Permission(db.Model):
    per_id = db.Column(db.Integer, primary_key=True)
    per_name = db.Column(db.String(64), index=True, unique=True)
    desc = db.Column(db.Text)

    def __init__(self, per_name, desc):
        self.per_name = per_name
        self.desc = desc

