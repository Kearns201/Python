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
        self.window.title('豆瓣TOP排行榜爬虫系统')
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
        self.bar.add_cascade(label='开始爬取排行榜', menu=self.new)
        # 将菜单栏放入主窗口
        self.window.config(menu=self.bar)
        # 定义表格
        self.tree = ttk.Treeview(self.window, columns=['排名', '电影名称', '链接', '评分', '评分人数'],
                                 show='headings')  # show='headings' 隐藏表头
        self.tree.pack(expand=1, fill='both')  # fill=both铺满左右窗口 expand表示上下也铺满
        # 定义列
        self.tree['columns'] = ('排名', '电影名称', '评分', '评分人数')
        # 设置列,不显示(设置列的属性格式)
        self.tree.column('排名', width=150, anchor='center')  # anchor=center文字居中
        self.tree.column('电影名称', width=150, anchor='center')
        self.tree.column('评分', width=150, anchor='center')
        self.tree.column('评分人数', width=150, anchor='center')
        # 显示表头(第一行标题文字)
        self.tree.heading('排名', text='排名')
        self.tree.heading('电影名称', text='电影名称')
        self.tree.heading('评分', text='评分')
        self.tree.heading('评分人数', text='评分人数')

    def add_thread(self):
        self.threa = threading.Thread(target=self.main)
        self.threa.start()

    def get_html(self, url):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.54'
                   }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return

    def get_infos(self, html):
        html = BeautifulSoup(html, "html.parser")
        # 排名
        num = html.select('#wrapper > div > div > div > ol.grid_view > li > div.item > div.pic > em')
        # 电影名字
        title = html.select('#wrapper > div> div > div> ol.grid_view > li > div.item > div.info' 
                            ' > div.hd > a > span.title:nth-child(1)')
        # 链接
        link = html.select('#wrapper > div > div > div > ol.grid_view > li > div.item > div.pic > a')
        # 评分
        rating_num = html.select('#wrapper > div > div > div.article > ol.grid_view > li'
                                 ' > div.item > div.info > div.bd > div.star>span.rating_num')
        # 评分人数
        evaluate_number = html.select('#wrapper > div > div > div.article > ol.grid_view > li'
                                      ' > div.item > div.info > div.bd > div.star>span:nth-child(4)')
        for n, t, l, r, e in zip(num, title, link, rating_num, evaluate_number):
            n = n.get_text()
            t = t.get_text()
            # l = l.get_text()
            r = r.get_text()
            e = e.get_text()
            self.tree.insert('', END, text='查找', values=(n, t, r, e))

    def main(self):
        items = self.tree.get_children()
        [self.tree.delete(item) for item in items]
        urls = ['https://movie.douban.com/top250?start={0}&filter='.format(str(i)) for i in range(0, 226, 25)]
        for url in urls:
            html = self.get_html(url)
            self.get_infos(html)
            time.sleep(0.5)


if __name__ == '__main__':
    bd = Gui()  # 调用主窗口类
    root = bd.window  # 创建窗口
    root.mainloop()  # 显示窗口
