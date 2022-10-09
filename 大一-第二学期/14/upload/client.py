import socket
import os
import struct

if __name__ == '__main__':
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input('请输入服务器的ip地址：')
    addr = (host, 9003)
    clientsocket.connect(addr)
    print('成功连接服务器')
    # 把文件发给服务器
    filename = input('请输入你要发送的文件：')
    filedir, name = os.path.split(filename)
    filesize = os.stat(filename).st_size
    # 发送文件名name和文件大小filesize
    filehead = struct.pack('128s1i', name.encode(), filesize)
    clientsocket.send(filehead)
    fp = open(filename, 'rb')
    while True:
        data = fp.read(1024)
        if not data:
            break
        clientsocket.send(data)
    print('文件已发送！')
    fp.close()
    clientsocket.close()
