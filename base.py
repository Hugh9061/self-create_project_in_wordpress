# 'base' class is the base of class which is used to create page and taxonomy.

import abc  # 利用abc模块实现抽象类

class Base(metaclass=abc.ABCMeta):

    def __init__(self, url='', item={'name' :'','slug':'','content':''}):
        self.url = url
        self.item = item

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, string):
        if not isinstance(string, str):
            raise TypeError('{}.url只能是字符串'.format([type(self)]))
        self.__url = string

    @property
    def item(self):
        return self.__item

    @item.setter
    def item(self, value):
        if not isinstance(value, dict):
            raise TypeError('{}item只能是字典数据'.format([type(self)]))
        if 'name' in value and 'slug' in value:    
            self.__item = value
        else :
            raise ValueError('{}.item字典必须带有 name 和 slug 字段'.format([type(self)]))

