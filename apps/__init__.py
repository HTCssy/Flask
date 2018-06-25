from flask import Flask

from apps.cache_one.views import init_cache
from apps.ext import config_db, init_ext, init_upload
from apps.home.converter import RegexConverter
from apps.home.views import home, init_home
from apps.login_one.views import init_login_one
from apps.search.views import init_search
from apps.shop.views import init_shop
# from apps.shop_6_20.views import init_shop_6_20
from apps.user.views import user, init_user
from apps.user_6_20.views import init_user_6_20

#flask实例化对象
app = Flask(__name__)
app.debug = True
#注册自定义转化器
app.url_map.converters['regex'] = RegexConverter
def create_app():
    #注册蓝图
    register_blue(app)
    init_ext(app)
    '''
    参数
    参数一 蓝图实例化对象
    参数二 注册
    '''
    return app
#统一注册所有蓝图对象
def register_blue(app):
    init_user(app)
    init_home(app)
    init_search(app)
    init_user_6_20(app)
    init_shop(app)
    # init_shop_6_20(app)
    init_cache(app)
    init_login_one(app)
    init_upload(app)




