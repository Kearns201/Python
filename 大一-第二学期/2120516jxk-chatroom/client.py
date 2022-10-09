import socket
import sys
import threading


class MychatClient():
    def __init__(self, host, post=9999, timeout=10):
        self.serverhost = host
        self.serverpost = post
        self.buffersize = 1024
        self.clienttimeout = timeout
        self.flag = 1
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientsocket.settimeout(self.clienttimeout)
        self.clientlock = threading.Lock()

    def send_msg(self):
        while True:
            data = sys.stdin.readline().strip()
            if data:
                self.clientsocket.sendall(data.encode())
            if data == 'exit':
                with self.clientlock:
                    self.flag = 0
                break
            self.clientsocket.sendall(data.encode())

    def recv_msg(self):
        while True:
            with self.clientlock:
                if self.flag == 0:
                    print('再见')
                    break
            try:
                data = self.clientsocket.recv(self.buffersize)
            except socket.timeout:
                continue
            except:
                raise
            if data:
                print('{0}\n'.format(data.decode()))

    def handle(self):
        self.clientsocket.connect((self.serverhost, self.serverpost))
        send_thread = threading.Thread(target=self.send_msg)
        recv_thread = threading.Thread(target=self.recv_msg)
        send_thread.start()
        recv_thread.start()
        send_thread.join()
        recv_thread.join()
        self.clientsocket.close()


if __name__ == '__main__':
    host = input('请输入服务器的地址:')
    port = 9003
    MychatClient(host, port).handle()
