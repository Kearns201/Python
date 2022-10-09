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
        self.window.title('酷狗排行榜爬虫系统')
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
        # 将菜单添加到菜单栏中，并添加标签
        self.bar.add_cascade(label='开始爬取排行榜', menu=self.new)
        # 将菜单栏放入主窗口
        self.window.config(menu=self.bar)
        # 定义表格
        self.tree = ttk.Treeview(self.window, show='headings')  # show='headings' 隐藏表头
        self.tree.pack(expand=1, fill='both')  # fill=both铺满左右窗口 expand表示上下也铺满
        # 定义列
        self.tree['columns'] = ('排名', '歌名—歌手', '播放时间')
        # 设置列,不显示(设置列的属性格式)
        self.tree.column('排名', width=50, anchor='center')  # anchor=center文字居中
        self.tree.column('歌名—歌手', width=300, anchor='center')
        self.tree.column('播放时间', width=100, anchor='center')
        # 显示表头(第一行标题文字)
        self.tree.heading('排名', text='排名')
        self.tree.heading('歌名—歌手', text='歌名—歌手')
        self.tree.heading('播放时间', text='播放时间')

    def add_thread(self):
        self.threa = threading.Thread(target=self.main)
        self.threa.start()

    def get_html(self, url):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0;Win64:x64) '
                                 'AppleWebKit/537.36(KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
                   }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return

    def get_infos(self, html):
        html = BeautifulSoup(html, "html.parser")
        ranks = html.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num')
        name = html.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
        time = html.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
        for r, n, t in zip(ranks, name, time):
            r = r.get_text().replace('\n', '').replace('\t', '').replace('\r', '')
            n = n.get_text()
            t = t.get_text().replace('\n', '').replace('\t', '').replace('\r', '')
            self.tree.insert('', END, text='查找', values=(r, n, t))

    def main(self):
        items = self.tree.get_children()
        [self.tree.delete(item) for item in items]
        urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1, 24)]
        for url in urls:
            html = self.get_html(url)
            self.get_infos(html)
            time.sleep(1)


if __name__ == '__main__':
    gui = Gui()  # 调用主窗口类
    root = gui.window  # 创建窗口
    root.mainloop()  # 显示窗口
