import socket

if __name__ == '__main__':
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = input('请输入服务器的IP地址:')
    addr = (host, 9003)
    clientsocket.connect(addr)
    print('成功连接服务器')
    # 把文件发给服务器
    filename=input('请输入你要发送的文件:')
    fp=open(filename,'rb')
    while True:
        data=fp.read(1024)
        if not data:
            break
        clientsocket.send(data)
    print('文件已发送')
    fp.close()
    clientsocket.close()