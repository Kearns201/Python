import queue
import socket
import time
from select import select

my_select_times = 100


class MychatServer:
    def __init__(self, host='127.0.0.1', port=9999, bufsize=1024):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverhost = host
        self.serverport = port
        self.serversocket.bind((self.serverhost, self.serverport))
        self.serversocket.listen()
        self.buffersize = bufsize
        self.inputs = [self.serversocket]
        self.outputs = []
        self.message_queues = {}
        self.client_info = {}

    def handle(self):
        while True:
            myinput, myoutput, myexception = select(self.inputs, self.outputs, self.inputs, my_select_times)
            if not (myinput, myoutput, myexception):
                continue
            for soc in myinput:
                if soc is self.serversocket:
                    clientsocket, clientaddr = soc.accept()
                    self.inputs.append(clientsocket)
                    self.client_info[clientsocket] = clientaddr
                    self.message_queues[clientsocket] = queue.Queue()
                else:  # soc客户端套接字
                    data = soc.recv(self.buffersize)
                    if data and data.decode() != 'exit':
                        data = '时间: %s客户端: %s发来信息: \n%s' % (time.strftime('%Y-%m-%d %H:%M:%S'),
                                                            self.client_info[soc], data.decode())
                        print(data)
                        self.message_queues[soc].put(data)
                        if soc not in self.outputs:
                            self.outputs.append(soc)
                    else:
                        print('客户端{0}:退出!'.format(self.client_info[soc]))
                        self.inputs.remove(soc)
                        if soc in self.outputs:
                            self.outputs.remove(soc)
                        del self.client_info[soc]
                        del self.message_queues[soc]
                        soc.close()
            for soc in myoutput:
                try:
                    next_msg = self.message_queues[soc].get_nowait()
                except queue.Empty:
                    self.outputs.remove(soc)
                else:
                    for client in self.client_info:
                        if client is not soc:
                            client.sendall(next_msg.encode())
            for soc in myexception:
                for soc in self.inputs:
                    self.inputs.remove(soc)
                    soc.close()
                if soc in self.outputs:
                    self.outputs.remove(soc)
                if soc in self.message_queues:
                    del self.message_queues[soc]
                del self.client_info[soc]


if __name__ == '__main__':
    host = ''
    MychatServer('', 9003, 1024).handle()
