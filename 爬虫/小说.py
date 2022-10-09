# coding:utf-8
import threading
import time
from tkinter import *
from tkinter import ttk

import requests
from bs4 import BeautifulSoup


class Gui(object):
    def __init__(self):
        self.window = Tk()
        self.window.title('小说系统')
        self.width = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 3
        self.height = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 4
        self.window.geometry('800x600+%d+%d' % (self.width, self.height))
        self.window.resizable(False, False)  # 控制窗口大小不可更改
        # 创建菜单栏
        self.bar = Menu()
        # 创建菜单
        self.new = Menu(self.bar, tearoff=0)  # 第二个参数是指去掉菜单和菜单栏之间的横线
        # 给关于菜单添加菜单栏
        self.new.add_command(label='开始', command=self.add_thread)
        # self.new.add_command(label='开始', command=self.main)
        # 将菜单添加到菜单栏中，并添加标签
        self.bar.add_cascade(label='开始获取', menu=self.new)
        # 将菜单栏放入主窗口
        self.window.config(menu=self.bar)
        # 定义表格
        self.tree = ttk.Treeview(self.window, columns=['小说'],
                                 show='headings')  # show='headings' 隐藏表头
        self.tree.pack(expand=1, fill='both')  # fill=both铺满左右窗口 expand表示上下也铺满
        # 定义列
        self.tree['columns'] = ('小说')
        # 设置列,不显示(设置列的属性格式)
        self.tree.column('小说', anchor='center')  # anchor=center文字居中
        # 显示表头(第一行标题文字)
        self.tree.heading('小说', text='小说')

    def add_thread(self):
        self.threa = threading.Thread(target=self.main)
        self.threa.start()

    def get_html(self, url):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54'
                   }
        self.response = requests.get(url, headers=headers)
        if self.response.status_code == 200:
            return self.response.text
        else:
            return

    def get_infos(self, html):
        html = BeautifulSoup(html, "html.parser")
        # 小说
        num = html.select('body>div>main>div.content>p')
        for n in zip(num):
            n = n.xpath('//div[@class="d_post_content j_d_post_content "]/text()').extract()
            self.tree.insert('', END, text='查找', values=n)
        self.page_text = self.response.text
        self.xs = self.xs + self.page_text
        fileName = '小说.txt'
        with open(fileName, 'w', encoding='utf-8')as fp:
            fp.write(self.xs)
        print(fileName, '保存成功!')

    def main(self):
        items = self.tree.get_children()
        [self.tree.delete(item) for item in items]
        urls = ['https://www.6378896f5822.com/xiaoshuo/15481{}.html'.format(str(i)) for i in range(0, 2)]
        self.xs = ''
        for url in urls:
            html = self.get_html(url)
            self.get_infos(html)
            time.sleep(0.5)


if __name__ == '__main__':
    bd = Gui()  # 调用主窗口类
    root = bd.window  # 创建窗口
    root.mainloop()  # 显示窗口
