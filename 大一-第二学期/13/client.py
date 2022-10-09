import socket
import tkinter as tk
from tkinter import scrolledtext
import _thread


def btnsendclick(event):
    data = entry_info.get()
    clientsocket.send(data.encode())
    st.insert(tk.END, '{0}说:'.format(socket.gethostbyname(socket.gethostname())) + str(data) + '\n')


def recv_msg():
    while True:
        recvdata = clientsocket.recv(4096).decode()
        st.insert(tk.END, '{0}说：'.format(host) + str(recvdata) + '\n')


if __name__ == '__main__':
    root = tk.Tk(className="客户端")
    root.geometry("300x400+200+200")
    frame1 = tk.Frame(root)
    entry_info = tk.Entry(frame1, width='35')
    btnsend = tk.Button(frame1, text='发送', width='6')
    btnsend.bind('<1>', btnsendclick)
    entry_info.pack(side='left', padx='5')
    btnsend.pack(side='left')
    frame1.pack(side='top')
    frame2 = tk.Frame(root)
    st = scrolledtext.ScrolledText(frame2)
    st.pack(expand=1, fill='both')
    frame2.pack(expand=1, fill='both')
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input('请输入服务器的IP地址:')
    addr = (host, 9999)
    clientsocket.connect(addr)
    print('成功连接服务器')
    _thread.start_new_thread(recv_msg, ())
    root.mainloop()
