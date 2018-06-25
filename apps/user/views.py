#控制层
#蓝图技术主要是拆分路由系统
'''
1,实例化蓝图对象
Blueprint()
2,使用flask对象注册蓝图
3,使用蓝图对象.route方法

'''
from flask import Blueprint, render_template

from apps.ext import db
from .models import User

user = Blueprint('user', __name__, static_folder='static', template_folder='templates', )
#注册
def init_user(app):
    app.register_blueprint(user, url_prefix='/user')

@user.route('/login_one/')
def login():
    user = User(name='老王',)
    db.session.add(user)
    db.session.commit()
    return render_template('index.html', msg='天气不错')


'''
查表  行跟列的组合
查询所有  select * from 表  
  select 列 列 from 表  

'''
@user.route('/find/')
def find():
    #通过id查询对象.控制列
    user = User.query.get(1)
    User.query.all()
    User.query.filter(User.name == '老王').first()
    return render_template('index.html', user=user)