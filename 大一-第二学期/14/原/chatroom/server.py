import socket
import select
import queue
import time
my_select_timeout=100
class MyChatServer():
    def __init__(self,host='127.0.0.1',port=9001,timeout=10,client_nums=10):
        #定义服务器的私有实例变量

        #创建聊天服务器TCP套接字

        #初始化服务器端列表对象



    def handle(self):


if __name__ == '__main__':
    host=''
    port=9001
    timeout=50
    client_nums=5
    MyChatServer(host,port,timeout,client_nums).handle()
