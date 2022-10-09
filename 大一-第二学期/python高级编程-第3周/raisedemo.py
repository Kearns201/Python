try:
    s = None
    if s is None:
        print('s是空对象')
        raise NameError
    print(len(s))
except TypeError:
    print('空对象没有长度')
