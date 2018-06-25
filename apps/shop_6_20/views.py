# from flask import Blueprint, request, render_template
# from flask import Flask
#
# from apps.ext import db
# from apps.user_6_20.models import UserShop
#
# shop_6_20 = Blueprint('shop', __name__, template_folder='templates')
#
# def init_shop_6_20(app:Flask):
#     app.register_blueprint(shop_6_20)

# #/list/1/10
# @shop_6_20.route('/list/')
# def list():
#     #get请求
#     #request.args
#     #post请求还有put
#     #request.from
#     #通用
#     page = request.values.get('page', default=1, type=int)
#     size = request.values.get('size', default=10, type=int)
#     paginate = db.session.query(UserShop.sid, UserShop.name).order_by(UserShop.sid).paginate(page=page, per_page=size,error_out=False)
#     shops = paginate.items
#     return render_template('shop_6_20.html', shops=shops, paginate=paginate)




