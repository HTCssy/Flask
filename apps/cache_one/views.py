from flask import Blueprint, Flask, render_template

from apps.ext import cache

cache_one = Blueprint('cache', __name__, template_folder='templates')

'''
timeout  过期时间
key_prefix 缓存key的前缀
unless 回掉函数 当返回True 缓存不起作用 None 使用缓存
'''
def init_cache(app:Flask):
    app.register_blueprint(cache_one)

@cache_one.route('/123/')
@cache.cached(timeout=60, key_prefix='')
def test():
    print('天台见')
    return '缓存成功'

'''
make_name 是一个函数  返回string类型  默认情况下会函数名称作为key缓存起来
'''
@cache_one.route('/121/<name>/')
#传参用这个
@cache.memoize(timeout=60*60)
def test2(name):
    print(name)
    return '缓存成功'

@cache_one.route('/110/')
def test3():
    return render_template('cache.html', msg='110')