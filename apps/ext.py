#实例化sqlalchemy对象
#配置连接数据库的参数
#注册SQLAlchemy对象
from flask_caching import Cache
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

db = SQLAlchemy()
#实例化迁移对象
migrate = Migrate()

def init_ext(app):
    #配置数据库
    config_db(app)
    #初始化SQLAlchemy
    db.init_app(app)
    #注册迁移命令
    migrate.init_app(app=app, db=db)
    #初始化缓存配置
    init_cache_congif(app)
    # 初始化用户管理模块
    init_login(app)
    #文件上传配置
    init_upload(app)

#配置数据库连接参数
def config_db(app):
    #配置数据库连接的url地址
    #地址格式  mysql+pymysql://用户名root:密码123456@127.0.0.1:3306/flask?charset=utf8
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = '1311311313131'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask_main?charset=utf8'




#缓存配置
cache = Cache()
def init_cache_congif(app):
    cache.init_app(app, config={
                                'CACHE_DEFAULT_TIMEOUT': 1*60,
                                'CACHE_TYPE': 'redis',
                                'CACHE_REDIS_HOST': '127.0.0.1',
                                'CACHE_REDIS_PORT': 6379,
                                # 'CACHE_REDIS_PASSWORD': '123456',
                                'CACHE_REDIS_DB': 1,
                                'CACHE_REDIS_PREFIX': 'view_'
    })


#免登陆插件
login_manager = LoginManager()
def init_login(app):
    #当用户点击某个需要登陆才能访问的界面时候,如果没用登陆,就会自动跳转相应视图函数
    login_manager.login_view = 'login_one.register'
    login_manager.login_message = '必须登陆才能访问'
    login_manager.init_app(app)


#文件上传相关配置\
'''
参数说明
    name : 保存文件的 子目录 默认是files
    extensions 设置允许上传文件的类型 默认类型
    default_dest 设置文件上传的根路径
'''
#可以配置多个
images = UploadSet(name='images', extensions=IMAGES, default_dest=None)
import os
'''配置信息'''
BDSE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_ROOT_PATH = os.path.join(BDSE_DIR, 'media/upload')
#1.配置上传的文件的根目录

def init_upload(app):
    #配置上传根目录
    app.config['UPLOADS_DEFAULT_DEST'] = UPLOAD_ROOT_PATH
    #生成文件的访问地址url
    # app.config['UPLOADS_DEFAULT_URL'] = ''

    '''
    app  Flask对象
    upload_sets 文件上传核心类 UploadSet
    '''
    configure_uploads(app=app, upload_sets=images)
    #限制文件上传的大小
    patch_request_class(app=app, size=64*1024*1024) #64M