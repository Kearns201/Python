import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = ''
port = 9999
addr = (host, port)
serversocket.bind(addr)
serversocket.listen(2)
clientsocket,clientaddr=serversocket.accept()
print('已连接到客户端',clientaddr)
recvdata=clientsocket.recv(4096).decode()
print('客户端说:',recvdata)
senddata=input('请输入要回复的信息:')
clientsocket.send(senddata.encode())
clientsocket.close()
serversocket.close()