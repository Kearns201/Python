# coding:utf-8

import sqlite3
from tkinter import *

conn = sqlite3.connect('D:\\Python\\myaddress.db')
# messagebox.showinfo('提示','数据库连接成功')

root = None


class Database:
    def __init__(self, master):
        self.master = master
        self.window = Tk()
        self.window.title('数据库管理系统')
        self.window.geometry('800x600+400+200')
        self.sname = ''
        # 创建菜单栏
        self.bar = Menu()
        # 创建菜单
        self.add = Menu(self.bar)
        # 给关于菜单添加菜单栏
        self.add.add_command(label='添加', command=self.getinput)
        # 将菜单添加到菜单栏中，并添加标签
        self.bar.add_cascade(label='添加', menu=self.add)
        # 将菜单栏放入主窗口
        self.window.config(menu=self.bar)
        # self.st = tkst.Scrolledtext(self.window, )
        # self.st.pack(expand=1, fill='both')

    def getinput(self):
        self.window = Tk()  # 建立窗口window
        self.window.title('数据编辑')  # 窗口名称
        self.window.geometry("400x240")  # 窗口大小(长＊宽)

        self.frame1 = Frame(self.window)
        self.label_id = Label(self.window, bg='#aFB1B3')
        self.label_id['width'] = 40
        self.label_id['text'] = '请输入iD'
        self.label_id.pack()
        self.text_id = StringVar()
        self.text_id = Text(self.window, height=1, width=40)  # 文本输入框
        self.text_id.pack()  # 把text放在window上面，显示text这个控件
        self.frame1.pack()

        self.btnRead = Button(self.window, height=1, width=20, text="确定", command=self.addclick)
        self.btnRead.pack()  # 显示按钮
        self.window.mainloop()  # 显示窗口

    def addclick(self):
        # 请输入编号：
        id = self.text_id.get()  # 获取文本框输入的内容
        print(id)


if __name__ == '__main__':
    rootedit = Database(root)
    root = rootedit.window
    root.mainloop()
    conn.close()
