# 小文是用来收集同一种类型文件的机器人

import os


class XiaoWen():
    def __init__(self,folder,file_type = 'html'):
        #collections 用来存放采集的文件地址
        self.collections = [] 
        self.folder = folder
        self.file_type = file_type
    
    # 加入指定类型的单个文件
    def add_item(self,item):
        if isinstance(item,str):
            if item.endswith(self.file_type):
                self.collections.append(item)
            else:
                print('{} : 文件类型不对，并未加入任务队列'.format(__name__))
        else:
            raise(TypeError('{}  :  {}.item只能是路径地址'.format(__name__,type(self))))

    # 插入多个文件
    def add_items(self,items):
        if isinstance(items,list):
            for item in items:
                if self.check(item):
                    if item.endswith(self.file_type):
                        self.collections.append(item)
                    else:
                        print('{}  :  item非html文件，并未录入'.format(__name__))
        else:
            raise(TypeError('{}  :  {}.items只能是列表'.format(__name__,type(self))))
            
    def check(self,item):
        if isinstance(item,str):
            if item.endswith(self.file_type):
                return True
            return False
        raise(TypeError('{}  :  {}.item只能是路径地址'.format(__name__,type(self))))
    
    def collect(self,path = ''):
        # 如果没有路径，默认使用Folder
        if not path:
            listdir = os.listdir(path= self.folder)
            self.add_items(listdir)
            return self.collections
        # 如果有路径，则使用path
        else:
            listdir = os.listdir(path=path)
            self.add_items(listdir)
            return listdir
        
    def collection(self):
        return self.collections
        
    
    @property 
    def file_type(self):
        return self.__file_type

    @file_type.setter
    def file_type(self,file_type):
        if not isinstance(file_type, str):
            raise TypeError('{}.file_type只能是字符串'.format([type(self)]))
        self.__file_type = file_type
        
    @property 
    def folder(self):
        return self.__folder
    
    @folder.setter
    def folder(self,path):
        if not isinstance(path, str):
            raise TypeError('{}.item只能是路径地址'.format(type(self)))
        self.__folder = path
        
    @property 
    def items(self):
        return self.__items
    
    @items.setter
    def items(self,lists):
        if not isinstance(lists, list):
            raise TypeError('{}.items只能是列表'.format(type(self)))
        self.__items = lists
        
        
if __name__ == "__main__":  
    path = 'C:/Users/LBDZ/Desktop/allFile/lb19005'   
    xiaowen = XiaoWen(path)
    xiaowen.collect()
    print(xiaowen.collections)
    
# XiaoWen.collection() 返回已经收集的html(默认)文件名称
# XiaoWen.collect(path=''), 若不传递参数，默认使用self.folder的地址，将数据分类
# XiaoWen.add_item(item) 用于向Xiaowen.collecionts加入一条数据 (item必须是字符串)
# XiaoWen.add_items(items)用于向XiaoWen.collections加入多条数据 (items必须是一个字符串列表)
# XiaoWen.Check(items) 检查对象是否属于XiaoWen.file_type

# XiaoWen 可以和select 搭配
# XiaoWen 负责采集文件， select 负责挑选文件