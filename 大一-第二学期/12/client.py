import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input('请输入服务器的IP地址:')
addr = (host, 9999)
clientsocket.connect_ex(addr)
print('成功连接服务器')
senddata=input('请输入要发送的信息:')
clientsocket.send(senddata.encode())
recvdata=clientsocket.recv(4096).decode()
print('服务器说:',recvdata)