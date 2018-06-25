from flask import Blueprint, request, abort, render_template

#实例化蓝图
home = Blueprint('home', __name__)
#注册
def init_home(app):
    app.register_blueprint(home)


@home.route('/')
def index():
    return '默认首页'


'''
'/test':表示重定向
正常写法:'/test/'
'''
@home.route('/test/')
def test1():
    return '带/和不带/的区别'

@home.route('/converter/<regex("\d{4}"):year>/')
def converter(year):
    print(year)
    return '自定义转化器'

#get 查  post 增  put 更新  delete 删除  key:values
@home.route('/method/', methods=['post', 'get', 'head'])#请求方式
def method():
    return '限制请求方式'


'''
全局错误处理
'''
@home.route('/1/')
def test2():
    if request.method == 'POST':
        pass
    else:
        return abort(400)

@home.errorhandler(404)
@home.errorhandler(400)
def error(e):
    if e.code == 404:
        return render_template('./errors/404.html')
    elif e.code == 400:
        return render_template('./errors/400.html')
    else:
        return render_template('./errors/')