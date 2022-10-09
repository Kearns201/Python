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
        st.insert(tk.END, '{0}说：'.format(clientaddr[0]) + str(recvdata) + '\n')


if __name__ == '__main__':
    root = tk.Tk(className="服务器")
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
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 9999
    addr = (host, port)
    serversocket.bind(addr)
    serversocket.listen(2)
    clientsocket, clientaddr = serversocket.accept()
    print('已经连接到客户端', clientaddr)
    _thread.start_new_thread(recv_msg, ())
    root.mainloop()
