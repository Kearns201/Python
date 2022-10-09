import tkinter as tk
import tkinter.scrolledtext as tkst
# from tkinter import messagebox, mydialog
from tkinter import filedialog
import fileinput
from tkinter import colorchooser
from tkinter import simpledialog
win=[]
root=None
class SimpleEditor:
    def __init__(self,master):
        if master==None:
            self.window=tk.Tk()
        else:
            self.window=tk.Toplevel(master)
        self.window.title('文本编辑器%d'%(len(win)+1))
        self.window.geometry('800x600')

        # root=None
        self.sname=''#初始文件名
        self.undonum=0
        #生成菜单栏bar
        self.bar=tk.Menu()
        #生成“文件”菜单
        self.filem=tk.Menu(self.bar)
        #向"文件"菜单添加菜单项
        self.filem.add_command(label='新建',command=self.neweditor)
        self.filem.add_command(label='打开',command=self.openfile)
        self.filem.add_command(label='保存',command=self.savefile)
        self.filem.add_command(label='另存',command=self.saveasfile)
        self.filem.add_separator()
        self.filem.add_command(label='关闭',command=self.close)
        #生成“编辑”菜单
        self.editm=tk.Menu(self.bar)
        #向"编辑"菜单添加菜单项
        self.editm.add_command(label="撤销",command=self.undo)
        self. editm.add_command(label="恢复",command=self.redo)
        self.editm.add_separator()
        self.editm.add_command(label="复制",command=self.copy)
        self.editm.add_command(label="粘贴",command=self.paste)
        self.editm.add_command(label="剪切",command=self.cut)
        self.editm.add_command(label="删除",command=self.delete)
        self.editm.add_separator()
        self.editm.add_command(label="查找",command=self.findstr)
        self.editm.add_command(label="替换",command=self.replacestr)
        self.editm.add_separator()
        self.editm.add_command(label='全选',command=self.select_all)
        #生成“设置”菜单
        self.formatm=tk.Menu(self.bar)
        #向"设置"菜单添加菜单项
        self.formatm.add_command(label="字体",command=self.setfont)
        self.formatm.add_separator()
        self.formatm.add_command(label="颜色",command=self.setcolor)
        self.formatm.add_separator()
        self.formatm.add_command(label='背景色',command=self.setbgcolor)
        #生成“关于”菜单
        self.aboutm=tk.Menu(self.bar)
        #向"关于"菜单添加菜单项
        self.aboutm.add_command(label="关于",command=self.about)
        #将菜单添加到菜单栏
        self.bar.add_cascade(label='文件',menu=self.filem)
        self.bar.add_cascade(label='编辑',menu=self.editm)
        self.bar.add_cascade(label='设置',menu=self.formatm)
        self.bar.add_cascade(label='关于',menu=self.aboutm)
        #将菜单栏添加到顶层（主）窗口
        self.window.config(menu=self.bar)
        self.st=tkst.ScrolledText(self.window,undo=True)
        self.st.focus()
        self.st.pack(expand=1,fill='both')
        # self.window.mainloop()
    def close(self):
        self.window.destroy()
    def about(self):
        messagebox.showinfo(title="关于文本编辑器",message="版本1.0，欢迎使用")
    def openfile(self):
        self.sname=filedialog.askopenfilename(filetypes=[("打开文件","*.txt")])
        if self.sname:
            for line in fileinput.input(self.sname):
                self.st.insert(tk.END,line)
                self.window.title(self.sname)
    def saveasfile(self):
        self.sname=filedialog.asksaveasfilename(title='保存文件',filetypes=[("保存文件","*.txt")])
        if self.sname:
            ofp=open(self.sname,"w")
            ofp.write(self.st.get(1.0,tk.END))
            ofp.flush()
            ofp.close()
            self.window.title(self.sname)
    def savefile(self):
        if self.sname:
            ofp=open(self.sname,'w')
            ofp.write(self.st.get(1.0,tk.END))
            ofp.flush()
            ofp.close()
        else:
            self.saveasfile()
    def neweditor(self):
        global root
        win.append(SimpleEditor(root))
    def setcolor(self):
        colors=colorchooser.askcolor()
        print(colors)
        self.st.config(fg=colors[1])
    def setbgcolor(self):
        colors=colorchooser.askcolor()
        self.st.config(bg=colors[1])
    def setfont(self):
        myfontdialog= mydialog.FontDialog(self.window)
        myfontdialog.wait_window()
        if mydialog.FONT:
            self.st.config(font=mydialog.FONT)
    def undo(self):
        text=self.st.get('1.0',tk.END)
        if len(text)<=1:
            return
        # self.st.edit_undo()
        self.st.event_generate('<<Undo>>')
        self.undonum=self.undonum+1
    def redo(self):
        if self.undonum==0:
            return
        # self.st.edit_redo()
        self.st.event_generate('<<Redo>>')
        self.undonum-=1
    def copy(self):
        self.st.event_generate('<<Copy>>')
        # try:
        #     ctext=self.st.get(tk.SEL_FIRST,tk.SEL_LAST)
        #     self.st.clipboard_clear()
        #     self.st.clipboard_append(ctext)
        # except tk.TclError:
        #     pass
    def paste(self):
        self.st.event_generate('<<Paste>>')
        # ptext=self.st.selection_get(selection='CLIPBOARD')
        # self.st.insert(tk.INSERT,ptext)
    def cut(self):
        self.st.event_generate('<<Cut>>')
        # cuttext=self.st.get(tk.SEL_FIRST,tk.SEL_LAST)
        # self.st.delete(tk.SEL_FIRST,tk.SEL_LAST)
        # self.st.clipboard_clear()
        # self.st.clipboard_append(cuttext)
    def delete(self):
        try:
            self.st.delete(tk.SEL_FIRST,tk.SEL_LAST)
        except tk.TclError as te:
            messagebox.showerror('操作错误','你没有选择要删除的文本！')
    def select_all(self):
        # self.st.event_generate('<<SelectAll>>')
        self.st.tag_add(tk.SEL,1.0,tk.END)
    def findstr(self):
        self.st.tag_remove('match', '1.0', 'end')
        self.st.tag_config('match',foreground='red',background='yellow')
        findtext=simpledialog.askstring('我的文本编辑器','请输入要查找的字符串')
        if findtext:
            start_pos='1.0'
            matchnum=0
            while True:
                start_pos=self.st.search(findtext,start_pos,stopindex='end',nocase=1)
                if not start_pos:
                    break
                end_pos='{}+{}c'.format(start_pos, len(findtext))
                self.st.tag_add('match',start_pos,end_pos)
                matchnum+=1
                start_pos=end_pos
        messagebox.showinfo(title='查找提示',message='发现%d个匹配的字符串'%matchnum)
    def replacestr(self):
        self.st.tag_remove('match', '1.0', 'end')
        self.st.tag_config('match', foreground='red', background='yellow')
        replacetext = simpledialog.askstring('我的文本编辑器', '请输入要查找的字符串和要替换的字符穿，用分号分开')
        if replacetext:
            tmp=replacetext.split(';')
            findstr=tmp[0]
            replacestr=tmp[1]
            if findstr=='':
                return
            start_pos = '1.0'
            find=[]
            findnum = 0
            while True:
                start_pos = self.st.search(findstr, start_pos, stopindex='end', nocase=1)
                if not start_pos:
                    break
                end_pos = '{}+{}c'.format(start_pos, len(findstr))
                find.append((start_pos,end_pos))
                findnum += 1
                start_pos = end_pos
            for item in reversed(find):
                self.st.delete(item[0],item[1])
                self.st.insert(item[0],replacestr)
                self.st.tag_add('match', item[0],'{}+{}c'.format(item[0], len(replacestr)))
        messagebox.showinfo(title='替换提示', message='共替换%d处' %findnum)
if __name__ == '__main__':
    win.append(SimpleEditor(root))
    root=win[0].window
    root.mainloop()