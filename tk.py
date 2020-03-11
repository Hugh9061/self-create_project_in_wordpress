import tkinter as tk
import setting
# 选择文件夹函数
from functions import selectPath,error,success,remove_label

class TK():
    def __init__(self):
        # 用于记录信息的数据
        self.list_iter = None
        self.current_item  =  None
        self.active_item = None
        self.result_list_page = []
        self.result_list_tax = []       
        
        # 用于记录文件夹信息的数据
        self.aim_folder = ''
        self.folder = ''
    # 选择文件夹
    def select_folder(self,option):
        window = tk.Tk()
        window.title('tk_grid')
        window.geometry('500x350')
        
        tk.Label(window,text='选择文件夹',width=40,height=3,font=20).grid(row=0,column=0,columnspan=3)

        tk.Label(window,text='文件夹路径:',width=20,height=3).grid(row=2,column=0)
        folder_name = tk.Entry(window,width=35,bd=4)
        folder_name.grid(row=2,column=1)
        tk.Button(window,text='目标路径',command=lambda:selectPath(folder_name)).grid(row=2,column=2)

        # 将目标文件夹的路径放入setting
        def submit():
            if folder_name.get():
                if option == 'FOLDER':
                    setting.FOLDER =  folder_name.get() + '/'
                    self.folder = folder_name.get() + '/'
                else :
                    setting.AIM_FOLDER = folder_name.get()
                    self.aim_folder = folder_name.get()
                print('{}  :  已经成功获取文件夹路径'.format(__name__))
                window.destroy()
            else:
                error_box = error(window=window,message="内容不能为空")
                error_box.place(x=100,y=50)
                time = 1
                threading.Timer(time,lambda:remove_label(error_box)).start()

        tk.Button(window, text='提交配置', width=30, height=3, command=submit).grid(
                row=4, column=1, columnspan=1, pady=5)
        window.mainloop()
    # 人工过滤
    def filter(self,lists):
        window = tk.Tk()
        # 将传过来的list变成可迭代
        self.list_iter = iter(lists)
        # 用于返回的result
        # 当前的item默认为第一个
        self.current_item = None
        try:
            self.current_item = next(self.list_iter)
            self.active_item = self.current_item
        except:
            print('空对象，无法使用')
            return None       
        window.title('页面创建器')
        window.geometry('800x500')
        
        # 消息队列
        message_box = tk.Text(master=window,width=40,height=33,bg='black',fg='yellow')
        message_box.grid(row=1, rowspan=7, padx=50, pady=10)

        # 名称
        tk.Label(window,text='name').grid(row=1, column=1, pady=5)
        name = tk.Entry(window, width=30,bd=4,	selectbackground = 'green')
        name.grid(row=1, column=2, pady=5)

        # 别名
        tk.Label(window,text='slug').grid(row=2, column=1, pady=5)
        slug = tk.Entry(window, width=30,bd=4,	selectbackground = 'green')
        slug.grid(row=2, column=2, pady=5)

        # 类别
        tax_label = tk.Label(window,text='tax')
        tax = tk.Entry(window, width=30,bd=4,	selectbackground = 'green')
    
        
        # 文章类型
        type_label = tk.Label(window,text='type')
        type_=tk.Entry(window, width=30,bd=4,	selectbackground = 'green')

        # 排列tax元素的先后顺序
        def sort_tax():
            tax_head = 0
            tax = self.result_list_tax
            for i in range(len(tax)):
                if tax[i]['name'] == tax[i]['tax']: #分类名称 与所属分类名字相同
                    tax[i],tax[tax_head] = tax[tax_head],tax[i]  #将该元素置列表前方
                    tax_head += 1
        # 在GUI界面展示当前内容信息
        def show():
            item = self.current_item
            name.delete(0,'end')
            name.insert(0,item['name'])
            slug.delete(0,'end')
            slug.insert(0,item['slug'])
            if 'tax' in item:
                tax_label.grid(row=3, column=1, pady=5)
                tax.grid(row=3, column=2, pady=5)
                type_label.grid(row=4, column=1, pady=5)
                type_.grid(row=4, column=2, pady=5)
                tax.delete(0,'end')
                tax.insert(0,item['tax'])
            else:
                tax.grid_forget()
                tax_label.grid_forget()
                type_.grid_forget()
                type_label.grid_forget()
        # 向结果列表添加元素
        def add_item():
            try:
                # 当前的item
                self.active_item = self.current_item
                # 指针偏移
                self.active_item['slug'] = slug.get()      
                page_type = '页面'          
                if 'tax' in self.active_item:
                    page_type = '分类'
                    self.active_item['tax'] = tax.get()
                    self.active_item['type'] = type_.get()
                    self.result_list_tax.append(self.active_item)
                    print('add-tax:',self.active_item['name']) #加入taxes列表
                else:
                    self.result_list_page.append(self.active_item) #加入pages列表
                    print('add-page:',self.active_item['name'])
                self.current_item = next(self.list_iter)
                message = '{}  :  已添加：\n {}   -   {} \n\n'.format(__name__,page_type,self.active_item['name'])
                message_box.insert('end',message)
                page_type = show()
            except:
                page_type = '页面'
                if 'tax' in self.current_item:
                    self.result_list_tax.append(self.current_item)
                    page_type = '分类'
                    self.current_item['tax'] = tax.get()
                    self.current_item['type'] = type_.get()
                    message = '{}  :  已添加：\n {}   -   {} \n\n'.format(__name__,page_type,self.current_item['name'])
                    message_box.insert('end',message)
                    sort_tax()
                else:
                    self.result_list_page.append(self.current_item)
                    message = '已添加：\n {}   -   {} \n\n'.format(page_type,self.current_item['name'])
                    message_box.insert('end',message)
                window.destroy()        
        # 跳过该元素，指向下一个元素
        def remove_item():
            try:
                # 指针偏移
                self.current_item = next(self.list_iter)
                show()
            except:
                sort_tax()
                window.destroy()

        tk.Button(window,text='添加',width=15,command=add_item).grid(row=5,column=1,pady=5)
        tk.Button(window,text='删除',width=15,command=remove_item).grid(row=5,column=2,pady=5)
        show()

        window.mainloop()

    