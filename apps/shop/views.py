from flask import Blueprint, Flask, render_template, request, redirect

from apps.ext import db
from .models import Shop

shop = Blueprint('shop', __name__, template_folder='templates', static_folder='static')

def init_shop(app:Flask):
    app.register_blueprint(shop, url_prefix=('/s'))

@shop.route('/find/<int:page>/<int:size>/')
def limit(page, size):
    paginate = Shop.query.filter(Shop.cate_id != 0).order_by(Shop.shop_id).paginate(page=page, per_page=size, error_out=True)
    shops = paginate.items
    return render_template('shop.html', shops=shops, paginate=paginate)

@shop.route('/search/', methods=['post'])
def search():
    shop_name = request.form.get('shop_name')
    shops = Shop.query.filter(Shop.name.like("%" + shop_name + "%")).filter(Shop.cate_id != 0).all()
    return render_template('search.html', shops=shops)

@shop.route('/add/', methods=['GET','POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        name = request.form.get('name')
        sub_title = request.form.get('sub_title')
        original_price = request.form.get('original_price')
        promote_price = request.form.get('promote_price')
        stock = request.form.get('stock')
        cate_id = request.form.get('cate_id')
        shop = Shop(name=name,
                    sub_title= sub_title,
                    original_price= original_price,
                    promote_price=promote_price,
                    stock=stock,
                    cate_id=cate_id
                    )
        db.session.add(shop)
        db.session.commit()
        return redirect('/s/find/1/10/')



@shop.route('/update/<int:shop_id>/', methods=['GET','POST'])
def update(shop_id):
    if request.method == 'GET':
        shop = Shop.query.filter_by(shop_id=shop_id).first()
        return render_template('update.html', shop=shop)
    elif request.method == 'POST':
        name = request.form.get('name')
        sub_title = request.form.get('sub_title')
        original_price = request.form.get('original_price')
        promote_price = request.form.get('promote_price')
        stock = request.form.get('stock')
        cate_id = request.form.get('cate_id')
        Shop.query.filter_by(shop_id=shop_id).update({'name': name,
                                                      'sub_title': sub_title,
                                                      'original_price': original_price,
                                                      'promote_price': promote_price,
                                                      'stock': stock,
                                                      'cate_id': cate_id
                                                      })
        db.session.commit()
        return '更新成功'


@shop.route('/delete/<int:shop_id>/', methods=['GET', 'POST'])
def delete(shop_id):
    #cate_id = 0时 表示删除 假删除
    # cate_id = 0
    #     # Shop.query.filter_by(shop_id=shop_id).update({'cate_id': cate_id})
    #     # db.session.commit()

    #物理删除
    shop = Shop.query.filter_by(shop_id=shop_id).first()
    db.session.delete(shop)
    db.session.commit()
    return redirect('/s/find/1/10/')