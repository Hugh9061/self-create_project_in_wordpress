# 小夏， 将由小文递交过来的数据用于筛选普通页面和分类页面

# 修改页面与分类的关系，就在这个文件中修改
from bs4 import BeautifulSoup
from xiaowen import XiaoWen
from functions import lists_single

class XiaoXia():

    def __init__(self, lists=[]):
        # page 和 tax初始化都为空
        self.pages = []
        self.taxes = []
        self.lists = lists

    def parse(self):  # 解析文件
        for item in self.lists:
            self.analysis(item)

    # is_tax   tax  page 三个函数的参数中的soup，必须传入的是BeautfulSoup的对象
    def is_tax(self, soup):
        if soup.find(class_='systitle-in'):
            return True
        return False

    def tax(self, soup):
        # 分类名
        title = soup.find('title').text
        # 分类父亲名
        parent = soup.find(class_='systitle-in').text
        #-----------------------------------------   在下面修改获取内容的条件 ----------------------------------------#
        content = soup.find(class_='w-main')      #这个是选择class = w-main的那个标签
        #-----------------------------------------   条件结束 -------------------------------------------------#
        tax = {
            'name': title,
            'slug': 'None',
            'tax': parent,
            'content':str(content)  #将选择的标签的内容tostring  并写入 content
        }
        self.taxes.append(tax)
        print('{}  :已添加添加{}分类'.format(__name__,title))

    def page(self, soup):
        title = soup.find('title').text
        #-----------------------------------------   在下面修改获取内容的条件 ----------------------------------------#
        content = soup.find(class_='w-main')      #这个是选择class = w-main的那个标签
        #-----------------------------------------   条件结束 -------------------------------------------------#
        page = {
            'name': title,
            'slug': 'None',
            'content' : str(content)
        }
        self.pages.append(page)
        print('{}  :已添加添加{}页面'.format(__name__,title))
    # analysis页面，不能为空
    def analysis(self, file_name):
        try:
            with open(file=file_name, mode='r', encoding='utf-8') as f:
                html = f.read()
        except:
            print('{}无法打开指定文件:'.format(__name__), file_name)
            return
        soup = BeautifulSoup(html, "html.parser")
        # 判断是否为分类页面，如果是,放入tax列表，否则放入page列表
        if self.is_tax(soup):
            self.tax(soup=soup)
        else:
            self.page(soup=soup)

    def set_single(self):
        self.pages = lists_single(self.pages)
        self.taxes = lists_single(self.taxes)

    @property
    def lists(self):
        return self.__lists

    @lists.setter
    def lists(self, value):
        if not isinstance(value, list):
            raise TypeError('{} : {}.value只能是列表'.format(__name__,type(self)))
        self.__lists = value


# XiaoXia.parse函数用来分类
#   如果给定file_path ，就会为file_path分类
#   若不给顶，则给自己的self.lists分类
