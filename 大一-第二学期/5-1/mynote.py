from tkinter import *
import tkinter.scrolledtext as tkst
from tkinter import messagebox
from tkinter import filedialog

root = None
n = 0


class SimpleEit:
    def __init__(self, master):
        global n
        self.undonum = 0
        if master == None:
            self.window = Tk()
        else:
            self.window = Toplevel(master)

        n += 1
        self.window.title('我的文本编辑器%d' % n)
        self.window.geometry('800x600+400+200')
        self.sname = ''
        # 创建菜单栏
        self.bar = Menu()
        # 创建四个菜单
        self.filem = Menu(self.bar)
        self.edutm = Menu(self.bar)
        self.formatm = Menu(self.bar)
        self.aboutm = Menu(self.bar)

        self.filem.add_command(label='新建', command=self.newfile)
        self.filem.add_command(label='打开', command=self.openfile)
        self.filem.add_command(label='保存', command=self.savefile)
        self.filem.add_command(label='另存', command=self.saveasfile)
        self.filem.add_separator()
        self.filem.add_command(label='关闭', command=self.close)

        self.edutm.add_command(label='撤销', command=self.undo)
        self.edutm.add_command(label='恢复', command=self.redo)
        self.edutm.add_separator()
        self.edutm.add_command(label='复制', command=self.copy)
        self.edutm.add_command(label='粘贴', command=self.paste)
        self.edutm.add_command(label='剪切', command=self.cut)
        self.edutm.add_command(label='删除', command=self.delete)
        self.edutm.add_separator()
        self.edutm.add_command(label='查找')
        self.edutm.add_command(label='替换')
        self.edutm.add_separator()
        self.edutm.add_command(label='全选', command=self.select_all)

        self.formatm.add_command(label='字体')
        self.formatm.add_separator()
        self.formatm.add_command(label='颜色')
        self.formatm.add_separator()
        self.formatm.add_command(label='背景色')
        # 给关于菜单添加菜单栏
        self.aboutm.add_command(label='关于', command=self.about)
        # 将菜单添加到菜单栏中，并添加标签
        self.bar.add_cascade(label='文件', menu=self.filem)
        self.bar.add_cascade(label='编辑', menu=self.edutm)
        self.bar.add_cascade(label='设置', menu=self.formatm)
        self.bar.add_cascade(label='关于', menu=self.aboutm)
        # 将菜单栏放入主窗口
        self.window.config(menu=self.bar)
        self.st = tkst.ScrolledText(self.window, undo=True)
        self.st.pack(expand=1, fill='both')
        # self.window.mainloop()

    def undo(self):
        # if len(self.st.get(1.0, END)) <= 1:
        #     return
        # self.undonum += 1
        # self.st.edit_undo()
        self.st.event_generate('<<Undo>>')

    def redo(self):
        # if self.undonum == 0:
        #     return
        # self.undonum -= 1
        # self.st.edit_redo()
        self.st.event_generate('<<Redo>>')

    def copy(self):
        # ctext=self.st.get(SEL_FIRST,SEL_LAST)
        # self.st.clipboard_clear()
        # self.st.clipboard_append(ctext)
        self.st.event_generate('<<Copy>>')

    def paste(self):
        # ptext=self.st.clipboard_get()
        # self.st.insert(INSERT,ptext)
        self.st.event_generate('<<Paste>>')

    def cut(self):
        self.st.event_generate('<<Cut>>')

    def delete(self):
        self.st.delete(SEL_FIRST, SEL_LAST)

    def select_all(self):
        self.st.event_generate('<<SelectAll>>')

    

    def close(self):
        self.window.destroy()

    def about(self):
        messagebox.showinfo(title='版本信息', message='版本1.0;版权所有:2120516')

    def saveasfile(self):
        self.sname = filedialog.asksaveasfilename(title='另存为', filetype=[('文本文件', '*.txt')])
        if self.sname != '':
            savefile = open(self.sname, 'w')
            savefile.write(self.st.get(1.0, 'end'))
            savefile.flush()
            savefile.close()

    def savefile(self):
        if self.sname != '':
            savefile = open(self.sname, 'w')
            savefile.write(self.st.get(1.0, 'end'))
            savefile.flush()
            savefile.close()
        else:
            self.savefile()

    def openfile(self):
        self.sname = filedialog.askopenfilename(filetype=[('文本文件', '*.txt')])
        openfile = open(self.sname, 'r')
        lines = openfile.readlines()
        self.st.delete(1.0, END)
        for line in lines:
            self.st.insert(END, line)

    def newfile(self):
        SimpleEit(root)


if __name__ == '__main__':
    rootedit = SimpleEit(root)
    root = rootedit.window
    root.mainloop()
