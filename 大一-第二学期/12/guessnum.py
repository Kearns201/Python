import tkinter as tk
import random
number=random.randint(100,999)
maxnum=999
minnum=100
def btnokclick(event):
    # print('你单击了确定按钮')
    global maxnum
    global minnum
    guessnum=int(entry_num.get())
    if guessnum==number:
        label_info['text']='恭喜猜对了！'
    elif guessnum>number:
        label_info['text']='大了哦'
        maxnum=guessnum
        label_range['text']='目前的范围是[%d,%d]'%(minnum,maxnum)
    else:
        label_info['text']='小了哦'
        minnum=guessnum
        label_range['text'] = '目前的范围是[%d,%d]' % (minnum, maxnum)

def btncloseclick():
    # print('你单击了关闭按钮')
    root.destroy()
def btnrestartclick(event):
    # print('你单击了重玩按钮')
    global maxnum
    global minnum
    global number
    maxnum=999
    minnum=100
    number=random.randint(100,999)
    label_info['text'] = '请输入100~999之间的任意整数'
    label_range['text'] = '目前的范围是[100,999]'
    entry_num.delete(0,'end')
    entry_num.focus()
root=tk.Tk(className='猜数字游戏')
root.geometry('400x150+400+200')
label_info=tk.Label(root,bg='#ffaaaa')
label_info['width']=40
label_info.pack()
label_range=tk.Label(root,bg='#aaffaa')
label_range['width']=40
label_range.pack()
frame1=tk.Frame(root)
entry_num=tk.Entry(frame1,width=20,font=('隶书','18'))
btnok=tk.Button(frame1,text='确定',width=6,font=('隶书','14'))
btnok.bind('<Button-1>',btnokclick)
entry_num.pack(side='left',padx=10)
btnok.pack()
frame1.pack()
frame2=tk.Frame(root)
btnclose=tk.Button(frame2,text='关闭',width=6,font=('隶书','14'),command=btncloseclick)
btnrestart=tk.Button(frame2,text='重玩',width=6,font=('隶书','14'))
btnrestart.bind('<1>',btnrestartclick)
btnclose.pack(side='left',padx=10)
btnrestart.pack()
frame2.pack()
label_info['text']='请输入100~999之间的任意整数'
label_range['text']='目前的范围是[100,999]'
entry_num.focus()
root.mainloop()