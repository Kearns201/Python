from tkinter import *  # 导入模块
from tkinter import messagebox

import requests

url = "http://1.1.1.3/ac_portal/login.php"  # 请求url

data = {  # 字符串参数
    "opr": "pwdLogin",
    "userName": "5521108",
    "pwd": "9c97aa89479f",
    "auth_tag": "1634968144880",
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
    "Referer": "http://1.1.1.3/ac_portal/20210315122758/pc.html?template="
               "20210315122758&tabs=pwd&vlanid=0&_ID_=0&switch_url=&url="
               "http://1.1.1.3/homepage/index.html&controller_type=&mac=4c-cc-6a-79-15-77",
    "X-Requested-With": "XMLHttpRequest"
}

if __name__ == '__main__':
    print("韩雨同学,请稍后,正在连接你的校园网账户......\n\n~~~///(^v^)\\\\\\~~~")
    root = Tk()  # 创建窗口
    root.withdraw()  # 隐藏主窗口
    resource = requests.post(url, data=data, headers=header).status_code  # 实现模拟登录
    if resource == 200:
        messagebox.showinfo(title="连接成功", message="回应代码{}\n你现在可以上网了哦(*^▽^*)".format(resource))
    else:
        messagebox.showinfo(title="连接失败", message="回应代码{}\n请在教室的客户机使用`(*>﹏<*)′".format(resource))
