'''
1> 登录  注销功能
2> 限制用户的权限
3> 记住密码功能
4> 对session进行保护
'''
from flask import Blueprint, render_template, request, redirect, abort, url_for, Flask
from flask_login import login_user, logout_user, login_required

from apps.ext import login_manager, db
from apps.login_one.models import UserLogin

from werkzeug.security import generate_password_hash,check_password_hash


"""
1>创建模型
2>配置登录
"""

login_one = Blueprint('login_one', __name__, template_folder='templates',static_folder='static')
def init_login_one(app:Flask):
    app.register_blueprint(login_one, url_prefix='/one')


#必写 得到uid
@login_manager.user_loader
def init_user(uid):
    user = UserLogin.query.get(uid)
    return user

@login_one.route('/main/')
#获取当前登录用户对象
def main():
    return render_template('main.html')

@login_one.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        password_ag = request.values.get('password_ag')
        email = request.values.get('email')
        if username and password and email:
            if password == password_ag:
                #密码加密
                pwd = generate_password_hash(password)
                user = UserLogin.query.filter(UserLogin.username == username).all()
                if not user:
                    userlogin = UserLogin(username=username, password=pwd, email=email)
                    db.session.add(userlogin)
                    db.session.commit()
                    # 必须调用第三方插件的login_user表示用户登陆成功
                    login_user(userlogin)
                    return redirect('/one/main/')
                else:
                    msg = '用户名已存在'
            else:
                msg = '两次输入密码不一致,重新输入'
        else:
            msg = '账户或密码不能为空'
    else:
        msg = '不支持的请求方式'
    return render_template('register.html', msg=msg)

@login_one.route('/login/', methods=['POST', 'GET'])
def login():
    msg = None
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        if username and password:
            try:
                user = UserLogin.query.filter(UserLogin.username == username).first()
                if user:
                    if check_password_hash(user.password, password):
                        #必须调用第三方插件的login_user表示用户登陆成功
                        login_user(user)
                        return redirect('/one/main/')
                    else:
                        msg = '密码错误'
                else:
                    msg = '用户不存在'
            except Exception as e:
                print(e)
                abort(500)
        else:
            msg = '账户或密码为空'
    else:
        msg = '不支持的请求方式'
    return render_template('login.html', msg=msg)

@login_one.errorhandler(404)
@login_one.errorhandler(400)
@login_one.errorhandler(500)
def error(e):
    if e.code == 404:
        return render_template('./errors/404.html')
    elif e.code == 400:
        return render_template('./errors/400.html')
    else:
        return render_template('./errors/error.html')

@login_one.route('/logout/')
def logout():
    logout_user()
    return redirect('/one/main/')

@login_one.route('/car/')
@login_required
def car():
    return '我的购物车'


