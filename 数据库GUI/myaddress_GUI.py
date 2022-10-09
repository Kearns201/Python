# coding:utf-8


import sqlite3
from re import compile
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# 新建数据表family
def new_click():
    try:  # 捕获异常
        conn.execute('''create table family
        (coding int primary key not null,
        name text not null,
        tele int not null,
        address text);''')
    except sqlite3.OperationalError:  # 抛出异常
        messagebox.showerror(title='新建错误', message='family数据表已经存在！')
    else:
        messagebox.showinfo('提示', '成功新建数据表family')


# 添加数据
def add_click():
    AddData()


# 修改数据
def modify_click():
    ModifyData()


# 删除数据
def delete_click():
    DeleteData()


# 数据库管理系统
class Database(object):
    frame_asc: Frame
    label_asc: Label
    button1_asc: Button
    button2_asc: Button
    button3_asc: Button
    button4_asc: Button
    frame_desc: Frame
    label_desc: Label
    button1_desc: Button
    button2_desc: Button
    button3_desc: Button
    button4_desc: Button

    def __init__(self):
        self.window = Tk()
        self.window.title('数据库管理系统')
        self.width = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 3
        self.height = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 4
        self.window.geometry('800x600+%d+%d' % (self.width, self.height))
        self.window.resizable(False, False)  # 控制窗口大小不可更改
        # 创建导航栏
        self.bar = Menu()
        # 创建菜单栏
        self.new = Menu(self.bar, tearoff=0)  # 第二个参数是指去掉菜单和菜单栏之间的横线
        self.find = Menu(self.bar, tearoff=0)
        self.add = Menu(self.bar, tearoff=0)
        self.modify = Menu(self.bar, tearoff=0)
        self.delete = Menu(self.bar, tearoff=0)
        self.sort = Menu(self.bar, tearoff=0)
        # 在菜单栏中添加菜单
        self.new.add_command(label='新建', command=new_click)
        self.find.add_command(label='查找', command=self.find_click)
        self.add.add_command(label='添加', command=add_click)
        self.modify.add_command(label='修改', command=modify_click)
        self.delete.add_command(label='删除', command=delete_click)
        self.sort.add_command(label='升序', command=self.sort_click_asc)
        self.sort.add_separator()  # 分割线
        self.sort.add_command(label='降序', command=self.sort_click_desc)
        # 将菜单添加到菜单栏中，并添加标签
        self.bar.add_cascade(label='新建', menu=self.new)
        self.bar.add_cascade(label='查找', menu=self.find)
        self.bar.add_cascade(label='添加', menu=self.add)
        self.bar.add_cascade(label='修改', menu=self.modify)
        self.bar.add_cascade(label='删除', menu=self.delete)
        self.bar.add_cascade(label='排序', menu=self.sort)
        # 将菜单栏放入主窗口
        self.window.config(menu=self.bar)
        # 定义表格
        self.tree = ttk.Treeview(self.window, columns=['编号', '姓名', '电话', '地址'], show='headings')  # show='headings' 隐藏表头
        self.tree.pack(expand=1, fill='both')  # fill=both铺满左右窗口 expand表示上下也铺满
        # 定义列
        self.tree['columns'] = ('编号', '姓名', '电话', '地址')
        # 设置列,不显示(设置列的属性格式)
        self.tree.column('编号', width=70, anchor='center')  # anchor=center文字居中
        self.tree.column('姓名', width=80, anchor='center')
        self.tree.column('电话', width=150, anchor='center')
        self.tree.column('地址', width=300, anchor='center')
        # 显示表头(第一行标题文字)
        self.tree.heading('编号', text='编号')
        self.tree.heading('姓名', text='姓名')
        self.tree.heading('电话', text='电话')
        self.tree.heading('地址', text='地址')

    # 查找数据
    def find_click(self):
        cursor = conn.cursor()  # 打开数据库
        try:  # 捕获异常
            my_list = cursor.execute('select * from family')
        except sqlite3.OperationalError:  # 抛出异常
            messagebox.showerror(title='查找错误', message='数据库中没有数据表family请点击新建')
        else:
            items = self.tree.get_children()
            [self.tree.delete(item) for item in items]
            for row in my_list:
                self.tree.insert('', END, text='查找依据:编号', values=(row[0], row[1], row[2], row[3]))
            items = self.tree.get_children()
            if not items:
                messagebox.showwarning(title='警告', message='数据库中没有数据')
            else:
                messagebox.showinfo(title='成功', message='查找完成')
        finally:
            cursor.close()  # 关闭数据库

    # 升序排序
    def sort_click_asc(self):
        cursor = conn.cursor()  # 打开数据库
        try:  # 捕获异常
            cursor.execute('select * from family')
        except sqlite3.OperationalError:  # 抛出异常
            messagebox.showerror(title='排序错误', message='数据库中没有数据表family请点击新建')
        else:
            self.window = Tk()  # 建立窗口window
            self.window.title('数据排序(升序)')  # 窗口名称
            self.width = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 2.25
            self.height = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 2
            self.window.geometry('400x240+%d+%d' % (self.width, self.height))  # 窗口大小(长＊宽)
            self.window.resizable(False, False)  # 控制窗口大小不可更改
            self.frame_asc = Frame(self.window)
            self.label_asc = Label(self.window, bg='#FC1944')
            self.label_asc['width'] = 45
            self.label_asc['text'] = '请选择排序依据'
            self.label_asc.pack()
            self.frame_asc.pack()
            self.button1_asc = Button(self.window, height=2, width=20, text="编号", bg='#FC5531',
                                      command=self.sort_asc_coding)
            self.button1_asc.pack()  # 显示按钮
            self.button2_asc = Button(self.window, height=2, width=20, text="姓名", bg='#D28E6B',
                                      command=self.sort_asc_name)
            self.button2_asc.pack()  # 显示按钮
            self.button3_asc = Button(self.window, height=2, width=20, text="电话", bg='#6a4158',
                                      command=self.sort_asc_tele)
            self.button3_asc.pack()  # 显示按钮
            self.button4_asc = Button(self.window, height=2, width=20, text="地址", bg='#FEC8BC',
                                      command=self.sort_asc_address)
            self.button4_asc.pack()  # 显示按钮
            self.window.mainloop()  # 显示窗口
        finally:
            cursor.close()  # 关闭数据库

    # 按coding升序排序
    def sort_asc_coding(self):
        self.window.destroy()  # 摧毁窗口
        cursor = conn.cursor()  # 打开数据库
        my_list = cursor.execute('select * from family order by coding asc')
        items = self.tree.get_children()
        [self.tree.delete(item) for item in items]
        for row in my_list:
            self.tree.insert('', END, text='排序依据:编号', values=(row[0], row[1], row[2], row[3]))
        items = self.tree.get_children()
        if not items:
            messagebox.showwarning(title='警告', message='数据库中没有数据')
        else:
            messagebox.showinfo(title='排序依据:编号', message='升序排序完成')
        cursor.close()  # 关闭数据库

    # 按name升序排序
    def sort_asc_name(self):
        self.window.destroy()  # 摧毁窗口
        cursor = conn.cursor()  # 打开数据库
        my_list = cursor.execute('select * from family order by name asc')
        items = self.tree.get_children()
        [self.tree.delete(item) for item in items]
        for row in my_list:
            self.tree.insert('', END, text='排序依据:姓名', values=(row[0], row[1], row[2], row[3]))
        items = self.tree.get_children()
        if not items:
            messagebox.showwarning(title='警告', message='数据库中没有数据')
        else:
            messagebox.showinfo(title='排序依据:姓名', message='升序排序完成')
        cursor.close()  # 关闭数据库

    # 按tele升序排序
    def sort_asc_tele(self):
        self.window.destroy()  # 摧毁窗口
        cursor = conn.cursor()  # 打开数据库
        my_list = cursor.execute('select * from family order by tele asc')
        items = self.tree.get_children()
        [self.tree.delete(item) for item in items]
        for row in my_list:
            self.tree.insert('', END, text='排序依据:电话', values=(row[0], row[1], row[2], row[3]))
        items = self.tree.get_children()
        if not items:
            messagebox.showwarning(title='警告', message='数据库中没有数据')
        else:
            messagebox.showinfo(title='排序依据:电话', message='升序排序完成')
        cursor.close()  # 关闭数据库

    # 按address升序排序
    def sort_asc_address(self):
        self.window.destroy()  # 摧毁窗口
        cursor = conn.cursor()  # 打开数据库
        my_list = cursor.execute('select * from family order by address asc')
        items = self.tree.get_children()
        [self.tree.delete(item) for item in items]
        for row in my_list:
            self.tree.insert('', END, text='排序依据:地址', values=(row[0], row[1], row[2], row[3]))
        items = self.tree.get_children()
        if not items:
            messagebox.showwarning(title='警告', message='数据库中没有数据')
        else:
            messagebox.showinfo(title='排序依据:地址', message='升序排序完成')
        cursor.close()  # 关闭数据库

    # 降序排序
    def sort_click_desc(self):
        cursor = conn.cursor()  # 打开数据库
        try:  # 捕获异常
            cursor.execute('select * from family')
        except sqlite3.OperationalError:  # 抛出异常
            messagebox.showerror(title='排序错误', message='数据库中没有数据表family请点击新建')
        else:
            self.window = Tk()  # 建立窗口window
            self.window.title('数据排序(降序)')  # 窗口名称
            self.width = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 2.25
            self.height = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 2
            self.window.geometry('400x240+%d+%d' % (self.width, self.height))  # 窗口大小(长＊宽)
            self.window.resizable(False, False)  # 控制窗口大小不可更改
            self.frame_desc = Frame(self.window)
            self.label_desc = Label(self.window, bg='#FC1944')
            self.label_desc['width'] = 45
            self.label_desc['text'] = '请选择排序依据'
            self.label_desc.pack()
            self.frame_desc.pack()
            self.button1_desc = Button(self.window, height=2, width=20, text="编号", bg='#FC5531',
                                       command=self.sort_desc_coding)  # 定义按键
            self.button1_desc.pack()  # 显示按钮
            self.button2_desc = Button(self.window, height=2, width=20, text="姓名", bg='#D28E6B',
                                       command=self.sort_desc_name)  # 定义按键
            self.button2_desc.pack()  # 显示按钮
            self.button3_desc = Button(self.window, height=2, width=20, text="电话", bg='#6a4158',
                                       command=self.sort_desc_tele)  # 定义按键
            self.button3_desc.pack()  # 显示按钮
            self.button4_desc = Button(self.window, height=2, width=20, text="地址", bg='#FEC8BC',
                                       command=self.sort_desc_address)  # 定义按键
            self.button4_desc.pack()  # 显示按钮
            self.window.mainloop()  # 显示窗口
        finally:
            cursor.close()  # 关闭数据库

    # 按coding降序
    def sort_desc_coding(self):
        self.window.destroy()  # 摧毁窗口
        cursor = conn.cursor()  # 打开数据库
        my_list = cursor.execute('select * from family order by coding desc')
        items = self.tree.get_children()
        [self.tree.delete(item) for item in items]
        for row in my_list:
            self.tree.insert('', END, text='排序依据:编号', values=(row[0], row[1], row[2], row[3]))
        items = self.tree.get_children()
        if not items:
            messagebox.showwarning(title='警告', message='数据库中没有数据')
        else:
            messagebox.showinfo(title='排序依据:编号', message='降序排序完成')
        cursor.close()  # 关闭数据库

    # 按name降序
    def sort_desc_name(self):
        self.window.destroy()  # 摧毁窗口
        cursor = conn.cursor()  # 打开数据库
        my_list = cursor.execute('select * from family order by name desc')
        items = self.tree.get_children()
        [self.tree.delete(item) for item in items]
        for row in my_list:
            self.tree.insert('', END, text='排序依据:姓名', values=(row[0], row[1], row[2], row[3]))
        items = self.tree.get_children()
        if not items:
            messagebox.showwarning(title='警告', message='数据库中没有数据')
        else:
            messagebox.showinfo(title='排序依据:姓名', message='降序排序完成')
        cursor.close()  # 关闭数据库

    # 按tele降序
    def sort_desc_tele(self):
        self.window.destroy()  # 摧毁窗口
        cursor = conn.cursor()  # 打开数据库
        my_list = cursor.execute('select * from family order by tele desc')
        items = self.tree.get_children()
        [self.tree.delete(item) for item in items]
        for row in my_list:
            self.tree.insert('', END, text='排序依据:电话', values=(row[0], row[1], row[2], row[3]))
        items = self.tree.get_children()
        if not items:
            messagebox.showwarning(title='警告', message='数据库中没有数据')
        else:
            messagebox.showinfo(title='排序依据:电话', message='降序排序完成')
        cursor.close()  # 关闭数据库

    # 按address降序
    def sort_desc_address(self):
        self.window.destroy()  # 摧毁窗口
        cursor = conn.cursor()  # 打开数据库
        my_list = cursor.execute('select * from family order by address desc')
        items = self.tree.get_children()
        [self.tree.delete(item) for item in items]
        for row in my_list:
            self.tree.insert('', END, text='排序依据:地址', values=(row[0], row[1], row[2], row[3]))
        items = self.tree.get_children()
        if not items:
            messagebox.showwarning(title='警告', message='数据库中没有数据')
        else:
            messagebox.showinfo(title='排序依据:地址', message='降序排序完成')
        cursor.close()  # 关闭数据库


# 添加数据
class AddData:
    def __init__(self):
        cursor = conn.cursor()  # 打开数据库
        try:  # 捕获异常
            cursor.execute('select * from family')
        except sqlite3.OperationalError:  # 抛出异常
            messagebox.showerror(title='添加错误', message='数据库中没有数据表family请点击新建')
        else:
            self.window = Tk()  # 建立窗口window
            self.window.title('数据添加')  # 窗口名称
            self.width = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 2.25
            self.height = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 2
            self.window.geometry('400x240+%d+%d' % (self.width, self.height))  # 窗口大小(长＊宽)
            self.window.resizable(False, False)  # 控制窗口大小不可更改
            # 容器1
            self.frame1 = Frame(self.window)
            self.label_name = Label(self.window, bg='#935167')
            self.label_name['width'] = 45
            self.label_name['text'] = '请输入姓名'
            self.label_name.pack()
            self.text_name = Entry(self.window, width='45')  # 文本输入框
            self.text_name.pack()  # 把text放在window上面，显示text这个控件
            self.frame1.pack()
            # 容器2
            self.frame2 = Frame(self.window)
            self.label_tele = Label(self.window, bg='#935167')
            self.label_tele['width'] = 45
            self.label_tele['text'] = '请输入电话号码'
            self.label_tele.pack()
            self.text_tele = Entry(self.window, width='45')  # 文本输入框
            self.text_tele.pack()  # 把text放在window上面，显示text这个控件
            self.frame2.pack()
            # 容器3
            self.frame3 = Frame(self.window)
            self.label_address = Label(self.window, bg='#FC1944')
            self.label_address['width'] = 45
            self.label_address['text'] = '请输入地址(暂时不输入请留空)'
            self.label_address.pack()
            self.text_address = Entry(self.window, width='45')  # 文本输入框
            self.text_address.pack()  # 把text放在window上面，显示text这个控件
            self.frame3.pack()
            # 确定按钮
            self.button = Button(self.window, height=2, width=20, text="确定", bg='#FC5531', command=self.append_click)
            self.button.pack()  # 显示按钮
            self.window.mainloop()  # 显示窗口
        finally:
            cursor.close()  # 关闭数据库

    def append_click(self):
        cursor = conn.cursor()  # 打开数据库
        # 获取编号：
        cursor.execute('select max(coding) from family')
        new_finds = cursor.fetchone()  # 自动获取上次数据库查询结果
        new_finds = new_finds[0]
        if new_finds is None:
            coding = int(1)
        else:
            coding = int(new_finds + 1)
        # 获取姓名：
        name = self.text_name.get()  # 获取文本框输入的内容
        # 获取电话号码：
        tele = self.text_tele.get()
        # 获取地址：
        address = self.text_address.get()
        if not (name or tele or address):
            messagebox.showwarning(title='无效操作', message='未检测到任何输入')
            cursor.close()  # 关闭数据库
            self.window.destroy()  # 摧毁窗口
        elif not name:
            messagebox.showinfo(title='姓名不能为空', message='请输入姓名')
            cursor.close()  # 关闭数据库
            self.window.destroy()  # 摧毁窗口
        elif not tele:
            messagebox.showinfo(title='手机号不能为空', message='请输入手机号')
            cursor.close()  # 关闭数据库
            self.window.destroy()  # 摧毁窗口
        elif not tele_structure.match(tele):
            messagebox.showwarning(title='手机号格式错误', message='请检查并输入正确的手机号')
            cursor.close()  # 关闭数据库
            self.window.destroy()  # 摧毁窗口
        else:
            cursor.execute('insert into family(coding,name,tele,address) values ((?),(?),(?),(?))',
                           (coding, name, tele, address))
            conn.commit()  # 提交数据更改
            messagebox.showinfo('提示', '成功添加一条记录')
            self.window.destroy()  # 摧毁窗口
            cursor.close()  # 关闭数据库


# 修改数据
class ModifyData:
    def __init__(self):
        cursor = conn.cursor()  # 打开数据库
        try:  # 捕获异常
            cursor.execute('select * from family')
        except sqlite3.OperationalError:  # 抛出异常
            messagebox.showerror(title='修改错误', message='数据库中没有数据表family请点击新建')
        else:
            cursor.execute('select max(coding) from family')
            new_finds = cursor.fetchone()  # 自动获取上次数据库查询结果
            new_finds = new_finds[0]
            if new_finds is None:
                messagebox.showerror(title='修改错误', message='数据表中没有任何数据')
            else:
                self.window = Tk()  # 建立窗口window
                self.window.title('数据编辑')  # 窗口名称
                self.width = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 2.25
                self.height = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 2
                self.window.geometry('400x270+%d+%d' % (self.width, self.height))  # 窗口大小(长＊宽)
                self.window.resizable(False, False)  # 控制窗口大小不可更改
                # 容器1
                self.frame1 = Frame(self.window)
                self.label_coding = Label(self.window, bg='#aFB1B3')
                self.label_coding['width'] = 45
                self.label_coding['text'] = '请输入需要修改的编号'
                self.label_coding.pack()
                self.text_coding = Entry(self.window, width='45')  # 文本输入框
                self.text_coding.pack()  # 把text放在window上面，显示text这个控件
                self.frame1.pack()
                # 容器2
                self.frame2 = Frame(self.window)
                self.label_name = Label(self.window, bg='#FC1944')
                self.label_name['width'] = 45
                self.label_name['text'] = '请修改姓名(默认不修改)'
                self.label_name.pack()
                self.text_name = Entry(self.window, width='45')  # 文本输入框
                self.text_name.pack()  # 把text放在window上面，显示text这个控件
                self.frame2.pack()
                # 容器3
                self.frame3 = Frame(self.window)
                self.label_tele = Label(self.window, bg='#FC1944')
                self.label_tele['width'] = 45
                self.label_tele['text'] = '请修改电话号码(默认不修改)'
                self.label_tele.pack()
                self.text_tele = Entry(self.window, width='45')  # 文本输入框
                self.text_tele.pack()  # 把text放在window上面，显示text这个控件
                self.frame3.pack()
                # 容器4
                self.frame4 = Frame(self.window)
                self.label_address = Label(self.window, bg='#FC1944')
                self.label_address['width'] = 45
                self.label_address['text'] = '请修改地址(默认不修改)'
                self.label_address.pack()
                self.text_address = Entry(self.window, width='45')  # 文本输入框
                self.text_address.pack()  # 把text放在window上面，显示text这个控件
                self.frame4.pack()
                # 定义按钮
                self.button = Button(self.window, height=2, width=20, text="确定", bg='#FC5531',
                                     command=self.modify_click)
                self.button.pack()  # 显示按钮
                self.window.mainloop()  # 显示窗口
        finally:
            cursor.close()  # 关闭数据库

    # 将修改数据写入数据表
    def modify_click(self):
        # 请输入编号：
        cursor = conn.cursor()  # 打开数据库
        try:  # 捕获异常
            change_coding = int(self.text_coding.get())  # 获取修改的编号
        except ValueError:  # 抛出异常
            messagebox.showwarning(title='警告', message='请确认是否正确输入编号')
        else:
            cursor.execute('select * from family where coding=?', (change_coding,))
            new_finds = cursor.fetchone()  # 自动获取上次数据库查询结果
            try:
                new_finds[0]
            except TypeError:
                messagebox.showerror(title='修改错误', message='数据表中没有这条记录')
            else:
                # 修改姓名
                new_name = self.text_name.get()
                new_tele = self.text_tele.get()
                new_address = self.text_address.get()
                if not (new_name or new_tele or new_tele):
                    messagebox.showinfo(title='无效操作', message='未检测到任何输入\n没有修改任何内容')
                else:
                    if not new_name:
                        pass
                    else:
                        cursor.execute('update family set name=? where coding=?', (new_name, change_coding))
                    # 修改电话
                    if not new_tele:
                        pass
                    else:
                        if tele_structure.match(new_tele):
                            cursor.execute('update family set tele=? where coding=?', (new_tele, change_coding))
                        else:
                            messagebox.showwarning(title='手机号格式错误', message='请检查并输入正确的手机号')
                            return
                    # 修改地址
                    if not new_address:
                        pass
                    else:
                        cursor.execute('update family set address=? where coding=?', (new_address, change_coding))
                    conn.commit()  # 提交数据更改
                    messagebox.showinfo('提示', '修改数据成功')
        finally:
            self.window.destroy()  # 摧毁窗口
            cursor.close()  # 关闭数据库


# 删除数据
class DeleteData:
    def __init__(self):
        cursor = conn.cursor()  # 打开数据库
        try:  # 捕获异常
            cursor.execute('select * from family')
        except sqlite3.OperationalError:  # 抛出异常
            messagebox.showerror(title='删除错误', message='数据库中没有数据表family请点击新建')
        else:
            self.window = Tk()  # 建立窗口window
            self.window.title('数据删除')  # 窗口名称
            self.width = (self.window.winfo_screenwidth() - self.window.winfo_reqwidth()) / 2.25
            self.height = (self.window.winfo_screenheight() - self.window.winfo_reqheight()) / 2
            self.window.geometry('400x240+%d+%d' % (self.width, self.height))  # 窗口大小(长＊宽)
            self.window.resizable(False, False)  # 控制窗口大小不可更改
            self.frame1 = Frame(self.window)
            self.label_coding = Label(self.window, bg='#aFB1B3')
            self.label_coding['width'] = 45
            self.label_coding['text'] = '请输入需要删除的编号(*表示删除所有表内数据)'
            self.label_coding.pack()
            self.text_coding = Entry(self.window, width='45')  # 文本输入框
            self.text_coding.pack()  # 把text放在window上面，显示text这个控件
            self.frame1.pack()
            self.button1 = Button(self.window, height=2, width=20, text="确定", bg='#FC5531',
                                  command=self.delete_click)  # 定义按钮
            self.button1.pack()  # 显示按钮
            self.button2 = Button(self.window, height=2, width=20, text="全部删除", bg='red',
                                  command=self.delete_all)  # 定义按钮
            self.button2.pack()  # 显示按钮
            self.window.mainloop()  # 显示窗口
        finally:
            cursor.close()  # 关闭数据库

    # 删除单条记录
    def delete_click(self):
        cursor = conn.cursor()  # 打开数据库
        delete_coding = self.text_coding.get()  # 获取文本框输入的内容
        if not delete_coding:
            messagebox.showinfo(title='提示', message='请输入你要删除的编号')
            self.window.destroy()  # 摧毁窗口
            cursor.close()  # 关闭数据库
        else:
            cursor.execute('select * from family where coding=?', (delete_coding,))
            new_finds = cursor.fetchone()  # 自动获取上次数据库查询结果
            try:
                new_finds[0]
            except TypeError:
                messagebox.showerror(title='删除错误', message='数据表中没有这条记录')
            else:
                choose = messagebox.askyesno(title='提示', message='你确定要删除这条记录吗')
                if not choose:
                    messagebox.showinfo('提示', '取消删除')
                    cursor.close()  # 关闭数据库
                else:
                    cursor.execute('delete from family where coding=?', (delete_coding,))
                    conn.commit()  # 提交数据更改
                    messagebox.showinfo('提示', '删除成功')
                    cursor.close()  # 关闭数据库
            finally:
                self.window.destroy()  # 摧毁窗口

    # 删除所有记录
    def delete_all(self):
        cursor = conn.cursor()  # 打开数据库
        self.window.destroy()  # 摧毁窗口
        choose = messagebox.askyesno(title='提示', message='你确定要删除所有表内数据吗')
        if not choose:
            messagebox.showinfo('提示', '取消删除')
            cursor.close()  # 关闭数据库
        else:
            cursor.execute('delete from family')
            conn.commit()  # 提交数据更改
            messagebox.showinfo('提示', '删除成功')
            cursor.close()  # 关闭数据库


if __name__ == '__main__':
    DBA = Database()  # 调用数据库管理系统主窗口类
    root = DBA.window  # 创建窗口
    conn = sqlite3.connect('my_address.db')  # 连接或创建数据库
    # messagebox.showinfo(title='提示', message='数据库连接成功')
    tele_structure = compile(r'^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
    root.mainloop()  # 显示窗口
    conn.close()  # 关闭数据库
