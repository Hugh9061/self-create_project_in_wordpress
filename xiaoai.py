# 小艾是用来自动化创建页面的机器人

from selenium import webdriver
from page import Page
from taxonomy import Taxonomy
import setting
import time

user = setting.USER
password = setting.PASSWORD


# 在出开始阶段，小艾会检擦自己的两个list是否为空，若为空，就不会执行

# 小艾执行任务，默认是从页面开始创建，其次是分类

# 在创建页面期间，每创建一个页面都小艾会检查自己的两个list任务是否为空，若为空，就会自动退出浏览器，执行 end


class XiaoAi():

    def __init__(self):
        self.page_task = []
        self.taxonomy_task = []
        self.login_status = False #用来标记是否已经登录过

    # 添加任务
    def add_task(self, obj):
        if isinstance(obj,Page):
            self.page_task.append(obj)
        elif isinstance(obj,Taxonomy):
            self.taxonomy_task.append(obj)
        else:
            print('{}  :  给定错误的任务对象,未放入任务队列'.format(__name__))

    # 开始执行阶段
    def start(self):
        # 检测两者是否为空
        if self.check_task():            
            self.browser = webdriver.Chrome()
            self.browser.set_window_size(1600,800)
            # 检查page里面的内容
            if self.check_page_task():
                self.create_page()
            # 最后检查taxonomy里面的内容
            if self.check_taxonomy_task():
                self.create_taxonomy()
            self.end()
        else:
            print('{}  :  无任务状态，现已退出'.format(__name__))

    # 结束阶段
    def end(self):
        self.browser.quit()

    # 检查任务是否存在
    def check_task(self):
        if self.page_task or self.taxonomy_task:
            return True
        return False

    # 检查页面任务是否存在
    def check_page_task(self):
        if self.page_task:
            return True
        return False

    # 检查分类任务是否存在
    def check_taxonomy_task(self):
        if self.taxonomy_task:
            return True
        return False

    # 登录
    def login(self, url):
        if not url:
            print('{}  :  url 为空','无法执行'.format(__name__))
            return
        # 若是处于未登录状态，则执行登录
        if not self.login_status:
            self.browser.get(url)
            time.sleep(1)
            login = self.browser.find_element_by_xpath('//input[@id="user_login"]')
            self.browser.find_element_by_xpath('//input[@id="user_login"]').send_keys(user)
            time.sleep(0.7)
            self.browser.find_element_by_xpath('//input[@id="user_pass"]').send_keys(password)
            time.sleep(0.7)
            self.browser.find_element_by_xpath('//input[@id="wp-submit"]').click()
            time.sleep(0.7)
            self.login_status = True

    # 创建页面
    def create_page(self):
        # 登录
        self.login(url=setting.LOGIN)
        time.sleep(1)
        # 执行任务
        while self.page_task:
            each = self.page_task.pop()
            self.browser.get(url=each.url)
            time.sleep(1)
            self.browser.find_element_by_xpath(each.title_path).send_keys(each.item['name'])
            time.sleep(1)
            self.browser.find_element_by_xpath(each.submit_path).click()
            time.sleep(1)
           
    #创建分类  
    def create_taxonomy(self):
        # 登录
        self.login(url=setting.LOGIN)
        time.sleep(1)
        # 将列表倒置
        self.taxonomy_task.reverse()
        # # 执行任务
        while self.taxonomy_task:
            time.sleep(1)
            each = self.taxonomy_task.pop()
            self.browser.get(url=each.url)
            # name
            self.browser.find_element_by_xpath(each.title_path).send_keys(each.item['name'])
            time.sleep(1)
            # slug
            self.browser.find_element_by_xpath(each.slug_path).send_keys(each.item['slug'])
            time.sleep(1)
            # tax
            if 'tax' in each.item:
                select = self.browser.find_element_by_xpath(each.select_path)
                options_list = select.find_elements_by_tag_name('option')
                for option in options_list:
                    if option.text == each.item['tax']:
                        option.click()
                        break
                time.sleep(1)
            # 提交
            self.browser.find_element_by_xpath(each.submit_path).click()
            time.sleep(2)
