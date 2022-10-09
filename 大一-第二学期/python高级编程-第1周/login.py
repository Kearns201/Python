dt = {'Alice': 'a123', 'Mike': 'good', 'John': '456', 'Kate': 'ktt'}
while True:
    print('用户登录和注册模拟')
    print('1.登录', end='  ')
    print('2.注册', end='  ')
    print('0.退出')
    choice = int(input('请输入你的选择（1，2）'))
    if choice == 0:
        exit(0)
    if choice == 1:
        count = 0
        while True:
            if count == 3:
                print('连续3次错误，退出登录！')
                exit(0)
            uname = input('请输入用户名：')
            if dt.get(uname) is not None:
                password = input('请输入密码：')
                if password == dt.get(uname):
                    print('成功登录')
                    break
                else:
                    print('密码不正确！')
            else:
                print('用户名不正确!')
            count = count + 1
    if choice == 2:
        while True:
            uname = input('请输入新的用户名：')
            if dt.get(uname) is not None:
                print('用户名已存在，请换个用户名！')
            else:
                break
        upass = input('请输入密码：')
        dt[uname] = upass
