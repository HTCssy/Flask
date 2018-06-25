from flask_script import Manager, Server
from flask import Flask

'''
原始的
'''
app = Flask(__name__)
#需要一个参数  flask对象的实例
manager = Manager(app)



#
# @app.route('/')
# def run():
#     return 'come'
#添加脚本
manager.add_command('start', Server(host='127.0.0.1', port=9000))


if __name__ == '__main__':
    manager.run()