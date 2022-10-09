import socket
import threading
import time
import sys
class MyChatClient(object):
    def __init__(self,host,port=9001,timeout=1,reconnect=2):
        #初始化私有实例变量


    def _connect(self):
        #创建客户端套接字



    def send_msg(self):


    def recv_msg(self):


    def handle(self):



if __name__ == '__main__':
    host=input('请输入服务器端的ip：')
    MyChatClient(host,9001,20,3).handle()
