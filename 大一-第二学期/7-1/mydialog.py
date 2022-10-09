from tkinter import *

FONT = ()


class FontDialog(Toplevel):
    def __init__(self, parent, title=None):
        Toplevel.__init__(self, parent)
        self.geometry('400x200+%d+%d' % (parent.winfo_rootx() + 50, parent.winfo_rooty() + 40))
        self.title('字体对话框')
        self.wm_attributes('-topmost', 1)
        self.resizable(width=False, height=False)
        self.grab_set()
        # 字体
        self.frame1 = Frame(self)
        Label(self.frame1, text='字体(F):').pack(anchor='w')
        self.fontnameshow = Label(self.frame1, bg='white', relief=SUNKEN, anchor='w')
        self.fontnameshow.pack(fill='x')
        self.fontlist = Listbox(self.frame1, width=20, height=5, selectmode=SINGLE)
        self.fontlist.bind('<<ListboxSelect>>', self.modifyfont)
        for item in ['宋体', '楷体', '黑体', '仿宋', '微软雅黑', '隶书', '华文彩云']:
            self.fontlist.insert('end', item)
        # self.fontlist.select_set(0)
        self.fontnameshow['text'] = self.fontlist.get(0)
        self.scrollbar1 = Scrollbar(self.frame1)
        self.scrollbar1.config(command=self.fontlist.yview)
        self.fontlist.pack(side='left')
        self.scrollbar1.pack(side='left', fill='y')
        self.frame1.grid(row=1, column=0, padx=20)
        # 字号
        self.frame2 = Frame(self)
        Label(self.frame2, text='大小(S):').pack(anchor='w')
        self.fontsizeshow = Label(self.frame2, bg='white', relief=SUNKEN, anchor='w')
        self.fontsizeshow.pack(fill='x')
        self.fontsizelist = Listbox(self.frame2, width=20, height=5, selectmode=SINGLE)
        self.fontsizelist.bind('<<ListboxSelect>>', self.modifysize)
        for item in range(10, 100):
            self.fontsizelist.insert('end', item)
        # self.fontsizelist.select_set(0)
        self.fontsizeshow['text'] = self.fontsizelist.get(0)
        self.scrollbar2 = Scrollbar(self.frame2)
        self.scrollbar2.config(command=self.fontsizelist.yview)
        self.fontsizelist.pack(side='left')
        self.scrollbar2.pack(side='left', fill='y')
        self.frame2.grid(row=1, column=1, padx=10)
        self.frame3 = Frame(self)
        self.btnok = Button(self.frame3, text='确定', width=8, command=self.btnokclick)
        self.btncancel = Button(self.frame3, text='取消', width=8, command=self.btncancelclick)
        self.btnok.pack(side='right', padx=20, pady=15)
        self.btncancel.pack(side='right')
        self.frame3.grid(row=2, columnspan=2, sticky='e')

    def modifyfont(self, event):
        if len(self.fontlist.curselection()) != 0:
            # print(self.fontlist.curselection())
            self.fontnameshow['text'] = self.fontlist.get(self.fontlist.curselection()[0])

    def modifysize(self, event):
        if len(self.fontsizelist.curselection()) != 0:
            # print(self.fontsizelist.curselection())
            self.fontsizeshow['text'] = self.fontsizelist.get(self.fontsizelist.curselection()[0])

    def btnokclick(self):
        global FONT
        FONT = (self.fontnameshow['text'], self.fontsizeshow['text'])
        self.destroy()

    def btncancelclick(self):
        self.destroy()
def askfont(parent):
    FontDialog(parent)
    return FONT


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x400+100+100")
    FontDialog(root)
    print(root.winfo_rootx())
    root.mainloop()
