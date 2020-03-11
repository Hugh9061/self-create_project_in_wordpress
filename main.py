from tk import TK
from xiaoai import XiaoAi
from xiaoxia import XiaoXia
from xiaowen import XiaoWen
from create import Create
import setting
from page import Page
from taxonomy import Taxonomy
import time

tk = TK()

# # 获取用户登录信息

tk.select_folder(option='FOLDER')
# -----------------------------------      小文       ------------------------------------------
# 将文件夹地址给小文,小文采集html文件
file_xiaowen = XiaoWen(folder=setting.FOLDER)               
file_xiaowen.collect()                                      
html_list = file_xiaowen.collection()

for i in range(len(html_list)):
    html_list[i] = setting.FOLDER + html_list[i]
    

# -----------------------------------      小夏       ------------------------------------------
# 将收集到的html_list交给小夏，小夏分析解析是页面还是分类
category_xiaoxia = XiaoXia(lists= html_list) 
category_xiaoxia.parse()   #解析文件,将文件信息打包成一个字典列表
category_xiaoxia.set_single()  #过滤列表中重复的字典

# 筛选出来的页面信息
pages = category_xiaoxia.pages
# 筛选出来的分类信息
taxes = category_xiaoxia.taxes


#####################     根据小夏筛选出来的分类信息，使用图形化人工过滤  #################################

if len(pages):
    tk.filter(pages)
    
time.sleep(1)
 
if len(taxes):
    tk.filter(taxes)

# 根据筛选出来的信息   实例化Page和Taxonomy对象
page = tk.result_list_page
tax = tk.result_list_tax



# 目标对象列表
aim_page = []
aim_tax = []

for item in page: #实例化页面
    aim_page.append(Page(item = item))
    
for item in tax:  #实例化分类
    aim_tax.append(Taxonomy(tax_name=item['type'],item=item))
    



# -----------------------------------      小艾       ------------------------------------------
xiaoai = XiaoAi()

# 将任务加入小艾的队列
for item in aim_page:
    xiaoai.add_task(item)

for item in aim_tax:
    xiaoai.add_task(item)

# 开始执行自动化生成
xiaoai.start()

# -----------------------------------      创建文件       ------------------------------------------

# 选择路径  设置为存储路径
# tk.select_folder('AIM_FOLDER')
# path = setting.AIM_FOLDER

total_list = page + tax
tk.select_folder('AIM_FOLDER')
# 创建文件
create = Create(folder=tk.aim_folder,file_list=total_list)
create.create_file()


