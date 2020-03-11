from tkinter import filedialog
from tkinter.filedialog import askdirectory
import tkinter as tk
from functools import reduce


# 将列表中的字典单一化
def lists_single(data_list):
    def run_function(x, y): return x if y in x else x + [y]
    return reduce(run_function, [[], ] + data_list)

# 传入一个Tk.Entry, 并将Tk.Entry中的值插入文件路径名
def selectPath(entry):   
    path = askdirectory()
    entry.insert(0, path)
    
#  tk Label标签创建全家桶
def error(window,message = '出现错误',width = 50,bg = 'black',fg = 'yellow',height = 3):   # 错误message
    error_message = tk.Label(window, text=message,fg=fg, width=width, bg=bg , height = height)
    return error_message

def success(window,message = '登陆成功',width = 50,bg = 'LightSeaGreen',fg = 'white',height = 3): # 成功message
    success_message = tk.Label(window, text=message,fg=fg, width=width, bg=bg , height = height)
    return success_message

def remove_label(label):  #label 是 tkinter 的控件
    label.destroy()

# 寻找符合html的标签，从起始到结束
def analysis_string(string, parameter, tag):
    """
    将一段符合规则的html替换，只替换默认的第一个
    :require string : HTML string
    :require parameter: substr in string
    :require tag: tag

    :return position: 一个元组，保存开始和结束的位置
    """
    # 左右标签闭合
    left = right = 0
    tag_L = tag
    tag_R = '/' + tag
    tag_length = len(tag)
    # 找到需要替换的起始位置
    start_position = string.find(parameter)
    if start_position == -1:
        return False, False

    # 标签结束位置
    end_position = start_position
    tag_end_position = end_position
    for char in string[start_position:]:
        if char == '<':
            if string[end_position + 1:end_position + tag_length + 1] == tag_L:
                left += 1
            elif string[end_position + 1:end_position + tag_length + 2] == tag_R:
                right += 1
                if(left == right):
                    end_position += tag_length + 2
                    break
        end_position += 1
    end_position += 1
    return start_position, end_position