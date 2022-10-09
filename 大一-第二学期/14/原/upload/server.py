import socketserver
class MyRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        #处理客户端的请求,接收文件

if __name__ == '__main__':
    host=''
    port=9003
    serverhost=(host,port)
    server=socketserver.TCPServer(serverhost,MyRequestHandler)
    server.serve_forever()