import setting
import tk
from functions import analysis_string


class Create():

    def __init__(self, folder, file_list=[]):
        self.folder = folder
        self.wait_create_list = file_list
        self.index_url = setting.FOLDER + '/index.php'

    # 普通文件
    def create_file(self):
        if not self.folder:
            print('Create穿过来的是空列表')
            return
        for item in self.wait_create_list:
            if 'tax' in item:  # 分类
                if item['name'] == item['tax']:
                    tax_filename = self.folder + \
                        '/tax-parts/' + item['slug'] + '.php'
                    single_filename = self.folder + \
                        '/single-parts/' + item['slug'] + '.php'
                    try:  # 创建分类和详情文件
                        with open(file=tax_filename, mode='w', encoding='utf-8') as f:
                            f.write(item['content'])  # 将内容写入
                        with open(file=single_filename, mode='w', encoding='utf-8') as f:
                            f.write(' ')
                        print('创建分类文件 : {}.php 成功'.format(item['slug']))
                    except:
                        print('创建分类文件失败:', tax_filename)
            else:  # 页面
                if item['slug'] != 'index':
                    page_filename = self.folder + \
                        '/page-parts/' + item['slug'] + '.php'
                    try:  # 创建页面文件
                        with open(file=page_filename, mode='w', encoding='utf-8') as f:
                            f.write(item['content'])  # 将内容写入
                        print('创建页面文件 : {}.php 成功'.format(item['slug']))
                    except:
                        print('创建页面文件失败:', page_filename)
                elif item['slug'] == 'index':
                    index_filename = self.folder + '/index.php'
                    try:  # 创建页面文件
                        with open(file=index_filename, mode='w', encoding='utf-8') as f:
                            f.write(item['content'])  # 将内容写入
                        print('写入文件 : {}.php 成功'.format(item['slug']))
                    except:
                        print('写入index页面失败')

    def create_header(self):
        html = self.read_index_html()
        (start, end) = analysis_string(
            html, '<div class="w-container w-main', 'div')  # 解析header结尾处
        if start:
            head_html = html.replace(html[start:], '')  # header内容
            (head_start, head_end) = analysis_string(
                head_html, '<head', 'head')  # 解析head标签内容
            if head_start:
                # 替换head标签内的内容为我们所需要的
                head_html.replace(
                    head_html[head_start:head_end], setting.file_head)
                try:
                    with open(self.folder + '/header.php', mode='w', encoding='utf-8') as f:
                        f.write(head_html)
                except:
                    print('打开文件失败：', self.folder + '/header.php')

    def create_footer(self):
        html = self.read_index_html()
        (start, end) = analysis_string(
            html, '<div class="w-container w-footer', 'div')  # 解析footer开始处
        if start:
            footer_html = html.replace(html[0:start], '')
            try:
                with open(self.folder + '/footer.php', mode='w', encoding='utf-8') as f:
                    f.write(head_html)
            except:
                print('打开文件失败：', self.folder + '/footer.php')

    def read_index_html(self):
        index_html = None
        try:
            with open(self.index_url, mode='r', encoding='utf-8') as f:
                index_html = f.read()
            return index_html
        except:
            print('失败读取文件')
            return False
