import sqlite3
conn=sqlite3.connect('database\\myaddress.db')
print('数据库连接成功')
while True:
    print('通讯录管理系统')
    print('1、新建',end=' ')
    print('2、查找',end=' ')
    print('3、添加',end=' ')
    print('4、修改',end=' ')
    print('5、删除',end=' ')
    print('6、排序',end=' ')
    print('0、退出')
    choice=int(input('请输入你的选择（0~6）：'))
    if choice==0:
        exit(0)
    elif choice==1:
        try:
            conn.execute('''create table family
            (id int primary key not null,
            name text not null,
            tele text not null,
            address text);''')
        except sqlite3.OperationalError as oe:
            print('数据表已经存在！')
        else:
            print('成功新建数据表')
    elif choice == 2:
        find=input('请输入你要查找的信息（*表示查找全部数据）：')
        cursor=conn.cursor()
        if find=='*':
            mylist=cursor.execute('select * from family')
        for row in mylist:
            print('编号：',row[0],end=' ')
            print('姓名：', row[1], end=' ')
            print('电话：', row[2], end=' ')
            print('地址：', row[3])
        cursor.close()
        print('查找完成')
    elif choice ==3:
        id=int(input('请输入编号：'))
        name=input('请输入姓名：')
        tele=input('请输入电话号码：')
        address=input('请输入地址：')
        cursor=conn.cursor()
        cursor.execute('insert into family(id,name,tele,address) values ((?),(?),(?),(?))',(id,name,tele,address))
        conn.commit()
        cursor.close()
        print('成功添加一条记录')
    elif choice == 4:
        print('修改数据表')
    elif choice == 5:
        print('删除数据表')
    elif choice == 6:
        print('排序数据表')