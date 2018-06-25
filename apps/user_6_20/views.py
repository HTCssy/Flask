from operator import and_, or_

from flask import Blueprint, Flask, request,render_template
import logging
from apps.ext import db
from apps.user_6_20.models import User_6_20, Cate, UserShop, Role, Permission

user_6_20 = Blueprint('user_6_20', __name__, template_folder='templates')

def init_user_6_20(app:Flask):
    app.register_blueprint(user_6_20)

'''
过滤函数
执行查询函数
'''
@user_6_20.route('/show/')
def show():
    #过滤列,只显示name这个列
    query = db.session.query(User_6_20.name).all()
    #查询所有的行跟列
    users = User_6_20.query.all()
    #过滤行
    user = User_6_20.query.filter_by(name='test1').first()
    #filter 可以使用运算符
    users = User_6_20.query.filter(User_6_20.name == 'xm').filter(User_6_20.uid == 1).all()
    #select uid,name from user where name='xm' and uid=1
    return '查询'

#过滤器  模糊查询
@user_6_20.route('/like/')
def filter_first():
    name = 'test'
    #sql语句%s%
    User_6_20.query.filter(User_6_20.name.like('%' + name + '%'))
    #s%
    users = User_6_20.query.filter(User_6_20.name.startswith('t')).all()
    logging.debug(users)
    #%s
    user = User_6_20.query.filter(User_6_20.name.endswith('1')).all()
    #IN       NOT IN
    User_6_20.query.filter(User_6_20.name.in_(['t', 's', 'c']))
    User_6_20.query.filter(~User_6_20.name.in_(['t', 's', 'c']))
    # is null   is not null
    User_6_20.query.filter(User_6_20.name is None)
    User_6_20.query.filter(User_6_20.name is not None)
    #and
    User_6_20.query.filter(and_(User_6_20.name == 'test1', User_6_20.weight > 120.00))
    User_6_20.query.filter(User_6_20.name == 'test1').filter(User_6_20.weight > 120.00)
    #or
    User_6_20.query.filter(or_(User_6_20.name == 'test1', User_6_20.weight > 120.00))
    return '常用的操作符'

'''
page  pagesize
分页
limit  表示去多少条数据
offset 表示偏移量  表示从设置的偏移量大小+1开始获取数据
计算最大页数
'''
@user_6_20.route('/limit/<int:page>/<int:size>/')
def query_limit(page, size):
    #注意:做分页的不需要设置执行函数
    #过滤列
    users = db.session.query(User_6_20.name, User_6_20.uid, User_6_20.create_date).order_by(User_6_20.uid).limit(size).offset((page - 1) * size)
    #总数据条数/每页条数=页数
    total = User_6_20.query.count() / size if  User_6_20.query.count() % size == 0 else  User_6_20.query.count() / size + 1
    print(total)
    users = User_6_20.query.order_by().slice((page - 1) * size, page * size)
    #################
    paginate = User_6_20.query.order_by(User_6_20.uid).paginate(page=page, per_page=size, error_out=False)
    #当前页面记录
    users = paginate.items
    #总共多少条
    print(paginate.total)
    #表示总共多少页
    print(paginate.pages)
    #获取当前选中的页数
    print(paginate.page)
    #上一页 下一页如果有就返回True 否则返回false
    print(paginate.has_prev)
    print(paginate.has_next)
    #显示页数列表
    paginate.iter_pages()
    return render_template('users.html', users=users, paginate=paginate)


#什么是事物:指的一系列操作, 这些操作要么一起成功要么全部失败

@user_6_20.route('/delete/')
def detele():
    user = User_6_20.query.fiter_by(name='test1').first()
    db.session.delete(user)
    #保存
    db.session.commit()
    return '删除成功'

@user_6_20.route('/add_first/')
def add_first():
    #增加数据(就相当于增加一个实例对象)
    user = User_6_20(name='健哥哥', weight=160.00, money=1000000.00)
    db.session.add(user)
    db.session.commit()
    return '添加成功'



@user_6_20.route('/save/')
def save_all():
    #批量添加
    # db.session.add_all()
    # # insert into user (name) values('test')
    objects = []
    for i in range(1, 101):
        objects.append(User_6_20(name='test'+ str(i)))
    db.session.bulk_save_objects(objects)
    db.session.commit()
    return '批量保存'

#根据条件先查询出对象
#更新
@user_6_20.route('/update/')
def update_one():
    user = User_6_20.query.filter_by(name='test1').first()
    user.name = '哥哥'
    db.session.commit()
    #同下
    # User_6_20.query.filter_by(name='test1').update({'name': '哥哥'})
    # db.session.commit()
    return '更新成功'

@user_6_20.route('/batch/')
def batch_update():
    User_6_20.query.filter(User_6_20.uid != 1).update({User_6_20.name: '哥哥'})
    #表示  四则运算
    User_6_20.query.filter(User_6_20.name == 'test1').update({User_6_20.money: User_6_20.money * 5}, synchroniz_session='evaluate')
    #表示字符串拼接
    User_6_20.query.filter(User_6_20.uid > 0).update({User_6_20.msg: '/upload' + User_6_20.msg}, synchroniz_session=False)
    db.session.commit()
    return '批量更新'






#############################################################

@user_6_20.route('/add/')
def add():
    cates = []
    for i in range(1, 6):
        cates.append(Cate(cname="分类" + str(i)))
    #批量添加
    db.session.bulk_save_objects(cates)
    db.session.commit()
    return '添加成功'
@user_6_20.route('/add1/')
def add1():
    shops = []
    for i in range(1, 6):
        shops.append(UserShop(name="商品" + str(i), cid=1))
    #批量添加
    db.session.bulk_save_objects(shops)
    db.session.commit()
    return '添加商品'


#通过一的一方查多的一方
'''
优点 一次查询就把多的一方加载出来
缺点 当数据够大的时候,会拖慢系统性能
'''
@user_6_20.route('/list/')
def find():
    cates = Cate.query.all()
    # for cate in cates:
    #     db.session.query(UserShop.name).filter(cid=cate.cid).all()
    #     #返回是个列表
    #     shop = cate.shops

    #主表查子表
    for shop in cates[0].shops:
        print(shop.name)

    #多的一方查一的一方,子表查主表
    # shop = db.session.query(UserShop.sid, UserShop.name, UserShop.cid).filter(UserShop.sid == 1).first()
    # cate = Cate.query.get(shop.cid)

    return '一对多'

#多的一方查一的一方,子表查主表
#/shop/?sid=1
@user_6_20.route('/usershop/')
def find_by_id():
    sid = request.values.get('sid', default=0, type=int)
    shop = UserShop.query.get(sid)
    print(shop.cate.cname)
    return '多对一'


######################################################
#多对多
#增删改查的权限
@user_6_20.route('/add/role')
def add_role():
    role = Role('admin', '超级管理员')
    db.session.add(role)
    db.session.add_all([
                        Permission('delete', '删除操作'),
                        Permission('update', '更新操作'),
                        Permission('insert', '添加操作'),
                        Permission('select', '查看操作'),
                        ])
    db.session.commit()
    return '添加权限角色'

@user_6_20.route('/add/role/per/')
def add_role_per():
    admin = Role.query.get(1)
    admin.permissions = Permission.query.all()
    db.session.commit()
    return '添加权限'

@user_6_20.route('/find/role/')
def find_role():
    role = Role.query.get(1)
    for per in role.permissions:
        print(per.per_name)
    return '通过角色查询权限'

@user_6_20.route('/del/msg/')
def del_msg():
    if has_per():
        return '删除成功'
    else:
        return '没有相关的权限'

def has_per():
    role = Role.query.get(1)
    for per in role.permissions:
        if per.per_name == 'delete':
            return True
    return False