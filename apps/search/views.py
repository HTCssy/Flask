from flask import render_template,Blueprint, Flask, request



search = Blueprint('search', __name__)


def init_search(app:Flask):
    app.register_blueprint(search, url_prefix='/search')



#注册自定义过滤器
# app.add_template_filter(add, 'add')
#注册自定义过滤器
# @search.add_app_template_filter('add')
def add(value, param2, param3):
    return value + param2 + param3




class Shop:
    def __init__(self, title, name):
        self.name = name
        self.title = title

@search.route('/temp/')
def temp1():
    shop = Shop(title='手机', name='华为')
    return render_template('search/search.html', li=[1, 2, 3],
                           dt={'name': '小明', 'age': 18},
                           shop=shop,
                           hello='world',)

@search.route('/fi/')
def filter1():
    return render_template('search/filter.html')

@search.route('/ext/')
def extend():
    return render_template('extends/extends.html')


@search.route('/for/')
def url_for():
    return render_template('search/for.html')


# http://127.0.0.1:9000/search/add/xm/
@search.route('/add/<name>/')
def add(name):
    return name