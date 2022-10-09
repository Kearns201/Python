import random
import tkinter as tk

number = random.randint(100, 900)
maxnum = 999
minnum = 100
running = True
num = 0


def btnGuessClick(event):
    global number
    global maxnum
    global minnum
    global running
    global num
    if running:
        answer = int(entry_num.get())
        if answer == number:
            label_info['text'] = '恭喜答对了！'
            num += 1
            running = False
            numGuess()
        elif answer < number:
            num += 1
            label_info['text'] = '小了哦'
            if answer > minnum:
                minnum = answer
            label_range['text'] = '目前的范围是[%d,%d]' % (minnum, maxnum)
        else:
            num += 1
            label_info['text'] = '大了哦'
            if answer < maxnum:
                maxnum = answer
            label_range['text'] = '目前的范围是[%d,%d]' % (minnum, maxnum)
    else:
        label_info['text'] = '您已经答对了！'


def numGuess():
    global num
    if num == 1:
        label_range['text'] = '好棒！一次答对！'
    elif num <= 10:
        label_range['text'] = '好厉害，尝试次数为%d次' % num
    elif num <= 20:
        label_range['text'] = '还行，尝试次数为%d次' % num
    else:
        label_range['text'] = '您都试了超过20次了，尝试次数为%d次' % num


def btnCloseClick(event):
    root.destroy()


def btnRestartClick(event):
    global number
    global running
    global num
    global maxnum
    global minnum
    number = random.randint(100, 999)
    running = True
    num = 0
    label_info['text'] = '请输入100到999之间的任意整数：'
    label_range['text'] = '目前的范围是[%d,%d]' % (minnum, maxnum)
    entry_num.delete(0, 'end')


root = tk.Tk(className="猜数字游戏")
root.geometry("400x150+200+200")
frame1 = tk.Frame(root)
label_info = tk.Label(frame1, width='40')  # 20个给定字体的字符宽度
label_info['bg'] = '#ffaaaa'
label_range = tk.Label(frame1, width='40')
label_range["bg"] = '#aaffaa'
label_info.pack()
label_range.pack()
frame1.pack(side='top')
frame2 = tk.Frame(root)
entry_num = tk.Entry(frame2, width='45')
btnGuess = tk.Button(frame2, text='确定', width='6')
entry_num.pack(side='left', padx='5')
btnGuess.pack(side='left')
btnGuess.bind('<1>', btnGuessClick)
entry_num.bind('<Return>', btnGuessClick)
frame2.pack(side='top')
frame3 = tk.Frame(root)
btnClose = tk.Button(frame3, text='关闭')
btnRestart = tk.Button(frame3, text='重玩')
btnClose.bind('<Button-1>', btnCloseClick)
btnClose.pack(side='left', padx='10')
btnRestart.bind('<Button-1>', btnRestartClick)
btnRestart.pack(padx='10')
frame3.pack()
label_info['text'] = '请输入100到999之间的任意整数：'
label_range['text'] = '目前的范围是[%d,%d]' % (minnum, maxnum)
entry_num.focus_set()
root.mainloop()
