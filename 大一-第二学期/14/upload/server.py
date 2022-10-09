import socketserver
import os
import struct

class MyRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        filehead = self.request.recv(1024)
        name, filesize = struct.unpack('128s1i', filehead)
        # 准备写文件
        newdir = 'D:\\receive'
        newname = name.decode().strip('\00')  # 接收文件名
        newfilename = os.path.join(newdir, newname)
        # 写文件
        fp = open(newfilename, 'wb')
        # 接收文件
        restsize = filesize
        while restsize > 0:
            if restsize < 1024:
                data = self.request.recv(restsize)
                restsize = 0
            else:
                data = self.request.recv(1024)
                restsize = restsize - 1024
            fp.write(data)
        print('文件上传成功!')
        fp.close()

if __name__ == '__main__':
    host = ''
    port = 9003
    serverhost = (host, port)
    server = socketserver.TCPServer(serverhost, MyRequestHandler)
    server.serve_forever()
