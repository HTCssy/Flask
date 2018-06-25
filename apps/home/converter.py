from werkzeug.routing import BaseConverter
'''
1.第一步 定义自定义转化器类 继承BaseConverter
2.注册自定义转化器
    app.url_map.converters['re'] = RegexConverter
3.使用
'''
import datetime


class RegexConverter(BaseConverter):

    def __init__(self, url_map, *args):
        super().__init__(url_map)
        #将第一个参数作为正则的匹配的规则
        self.regex = args[0]


    #将匹配到的值转化成python类型
    def to_python(self, value):
        return datetime.datetime.strptime(value, '%Y')