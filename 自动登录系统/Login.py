from tkinter import *  # 导入模块
from tkinter import messagebox

import requests

url = "http://1.1.1.3/ac_portal/login.php"  # 请求url

data = {  # 字符串参数
    "opr": "pwdLogin",
    "userName": "2120516",
    "pwd": "fd6da573a0be",
    "auth_tag": "1634287116150",
    "rememberPwd": "0",
}

header = {  # 请求标头
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/"
                  "537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "83",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "1.1.1.3",
    "Origin": "http://1.1.1.3",
    "Referer": "http://1.1.1.3/ac_portal/20210315122758/pc.html",
    "X-Requested-With": "XMLHttpRequest"
}

if __name__ == '__main__':
    print("请稍后,正在连接......")
    root = Tk()  # 创建窗口
    root.withdraw()  # 隐藏主窗口
    resource = requests.post(url, data=data, headers=header).status_code  # 实现模拟登录
    if resource == 200:
        messagebox.showinfo(title="连接成功", message="回应代码{}".format(resource))
    else:
        messagebox.showinfo(title="连接失败", message="回应代码{}".format(resource))
