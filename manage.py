from flask_script import Manager, Server
from flask import Flask
from flask_migrate import MigrateCommand

#需要一个参数  flask对象的实例
from apps import create_app
manager = Manager(create_app())

#添加脚本
manager.add_command('start', Server(host='127.0.0.1', port=9000))
#添加迁移的脚本
manager.add_command('db', MigrateCommand)



if __name__ == '__main__':
    manager.run()