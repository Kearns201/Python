import tkinter as tk
import random

number = random.randint(100, 999)
maxnum = 999
minnum = 100


def btnokclick(event):
    # print('你单机了确定按钮')
    global maxnum  # 全局变量global
    global minnum
    guessnum = int(entry_num.get())
    if guessnum == number:
        label_info['text'] = '恭喜猜对了!'
        label_range['text'] = '恭喜猜对了!'
    elif guessnum > number:
        label_info['text'] = '大了(⊙o⊙)'
        maxnum = guessnum
        label_range['text'] = '目前的范围是[%d,%d]' % (minnum, maxnum)
        entry_num.focus()
        entry_num.delete(0, 'end')
    else:
        label_info['text'] = '小了(⊙o⊙)'
        minnum = guessnum
        label_range['text'] = '目前的范围是[%d,%d]' % (minnum, maxnum)
        entry_num.focus()
        entry_num.delete(0, 'end')


def btncloseclick():
    print('你单机了关闭按钮')
    root.destroy()


def btnrestartclick(event):
    print('你单机了重玩按钮')
    global maxnum
    global minnum
    global number
    maxnum = 999
    minnum = 100
    number = random.randint(100, 999)
    label_info['text'] = '请输入100~999之间的任意整数'
    label_range['text'] = '目前的范围是100,999'
    entry_num.delete(0, 'end')
    entry_num.focus()


def entrynumreturn(event):#没必要
    btnok.focus()  # focus光标定位


root = tk.Tk(className='猜数字游戏')
root.geometry('400x150+400+200')
label_info = tk.Label(root, bg='#FFAAAA')
label_info['width'] = 40
label_info.pack()
label_range = tk.Label(root, bg='#AAFFAA')
label_range['width'] = 40
label_range.pack()
frame1 = tk.Frame(root)
entry_num = tk.Entry(frame1, width=20, font=('隶书', '18'))
btnok = tk.Button(frame1, text='确定', width=7, font=('隶书', '12'))
btnok.bind('<1>', btnokclick)
# entry_num.bind('<Return>', entrynumreturn)
entry_num.bind('<Return>', btnokclick)
# btnok.bind('<Return>', btnokclick)
entry_num.pack(side='left', padx=10)
btnok.pack()
frame1.pack()
frame2 = tk.Frame(root)
btnclose = tk.Button(frame2, text='关闭', width=7, font=('隶书', '12'), command=btncloseclick)
btnrestert = tk.Button(frame2, text='重玩', width=7, font=('隶书', '12'))
btnrestert.bind('<1>', btnrestartclick)
btnclose.pack(side='left', padx=10)
btnrestert.pack()
frame2.pack()
label_info['text'] = '请输入100~999之间的任意整数'
label_range['text'] = '目前的范围是100,999'
entry_num.focus()
root.mainloop()
