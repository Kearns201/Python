import tkinter as tk
from tkinter import messagebox


# import tkinter.messagebox
class RegisterForm:
    def __init__(self, master):
        frame = tk.Frame(master)
        frame.pack()
        tk.Label(frame, text='用户名').grid(row=0, column=0, pady=3)
        self.userAccount = tk.Entry(frame, width=20)
        self.userAccount.grid(row=0, column=1, padx=5)
        tk.Label(frame, text='密码').grid(row=1, column=0, pady=3)
        self.userPass = tk.Entry(frame, width=20, show='*')
        self.userPass.grid(row=1, column=1, padx=5)
        tk.Label(frame, text='确认密码').grid(row=2, column=0, pady=3)
        self.userPass2 = tk.Entry(frame, width=20, show='*')
        self.userPass2.grid(row=2, column=1, padx=5)
        tk.Label(frame, text='姓名').grid(row=3, column=0, pady=3)
        self.userName = tk.Entry(frame, width=20)
        self.userName.grid(row=3, column=1, padx=5)
        tk.Label(frame, text='证件类型').grid(row=4, column=0, pady=3)
        self.sc=tk.Scrollbar(frame)
        self.IDType = tk.Listbox(frame, height=2, width=20,yscrollcommand=self.sc.set)
        for item in ['身份证', '军人证', '护照']:
            self.IDType.insert('end', item)
        self.IDType.grid(row=4, column=1)
        self.IDType.select_set(0)
        # self.sc.config(command=self.IDType.yview)
        tk.Label(frame, text='证件号码').grid(row=5, column=0, pady=3)
        self.IDnumber = tk.Entry(frame, width=20)
        self.IDnumber.grid(row=5, column=1, padx=5)
        tk.Label(frame, text='邮箱').grid(row=6, column=0, pady=3)
        self.email = tk.Entry(frame, width=20)
        self.email.grid(row=6, column=1, padx=5)
        tk.Label(frame, text='手机号码').grid(row=7, column=0, pady=3)
        self.mobile = tk.Entry(frame, width=20)
        self.mobile.grid(row=7, column=1, padx=5)
        tk.Label(frame, text='单位性质').grid(row=8, column=0, pady=3)
        self.company = tk.IntVar()
        tk.Radiobutton(frame, variable=self.company, value=1, text='政府机构').grid(row=8, column=1, sticky='w')
        tk.Radiobutton(frame, variable=self.company, value=2, text='事业单位').grid(row=9, column=1, sticky='w')
        tk.Radiobutton(frame, variable=self.company, value=3, text='企业').grid(row=10, column=1, sticky='w')
        tk.Radiobutton(frame, variable=self.company, value=4, text='其他').grid(row=11, column=1, sticky='w')
        tk.Label(frame, text='擅长').grid(row=12, column=0, pady=5)
        self.special = [tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()]
        self.spelist = ['网络系统', 'web软件开发', '嵌入式开发', '云计算', '大数据应用']
        for i in range(4):
            tk.Checkbutton(frame, variable=self.special[i], onvalue=i + 1, text=self.spelist[i]).grid(row=12 + i,
                                                                                                      column=1,
                                                                                                      sticky='w')
        self.okBtn = tk.Button(frame, text='提交', command=self.check).grid(row=18, column=0, sticky='w')
        self.okBtn = tk.Button(frame, text='退出', command=frame.quit).grid(row=18, column=1, sticky='e')

    def check(self):
        if self.userPass.get() != self.userPass2.get():
            messagebox.showinfo('密码不正确', '您两次输入的密码不同，请重新输入')
            # tkinter.messagebox.showinfo()
            self.userPass.selection_clear()
            self.userPass2.selection_clear()
            self.userPass.icursor(0)
            return
        info = '您输入的信息如下：\n'
        info += '用户名：' + self.userPass.get() + '\n'
        info += '密码：' + self.userPass.get() + '\n'
        info += '姓名：' + self.userName.get() + '\n'
        info += '证件类型：' + self.IDType.get(self.IDType.curselection()) + '\n'
        info += '证件号码：' + self.IDnumber.get() + '\n'
        info += '邮箱：' + self.email.get() + '\n'
        info += '手机号码：' + self.mobile.get() + '\n'
        tmpList = ['政府机构', '事业单位', '企业', '其他']
        info += '单位性质：' + tmpList[self.company.get() - 1] + '\n'
        tmp = ''
        for i in range(len(self.spelist)):
            if self.special[i].get() != 0:
                tmp += self.spelist[i] + ';'
        info += '擅长：' + tmp + '\n'
        messagebox.showinfo('用户注册表反馈信息', info)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('用户注册表单')
    root.geometry('360x560+100+50')
    res = RegisterForm(root)
    root.mainloop()
