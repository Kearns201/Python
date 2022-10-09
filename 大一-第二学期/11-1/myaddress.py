import sqlite3

conn = sqlite3.connect('D:\\2120516jxk\\myaddress.db')
print('数据库连接成功')
while True:
    print('通讯录管理系统')
    print('1、新建', end=' ')
    print('2、查找', end=' ')
    print('3、添加', end=' ')
    print('4、修改', end=' ')
    print('5、删除', end=' ')
    print('6、排序', end=' ')
    print('0、退出')
    choice = int(input('请输入你的选择（0~6）：'))
    if choice == 0:
        # conn.close()
        # exit(0)
        break
    elif choice == 1:
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
        find = input('请输入你要查找的信息（*表示查找全部数据）：')
        cursor = conn.cursor()
        if find == '*':
            mylist = cursor.execute('select * from family')
        else:
            mylist = cursor.execute('select * from family where id=(?) or name like ? or tele like ? or address like ?', \
                                    (find, '%' + find + '%', '%' + find + '%', '%' + find + '%'))
        for row in mylist:
            print('编号：', row[0], end=' ')
            print('姓名：', row[1], end=' ')
            print('电话：', row[2], end=' ')
            print('地址：', row[3])
        cursor.close()
        print('查找完成')
    elif choice == 3:
        id = int(input('请输入编号：'))
        name = input('请输入姓名：')
        tele = input('请输入电话号码：')
        address = input('请输入地址：')
        cursor = conn.cursor()
        cursor.execute('insert into family(id,name,tele,address) values ((?),(?),(?),(?))', (id, name, tele, address))
        conn.commit()
        cursor.close()
        print('成功添加一条记录')
    elif choice == 4:
        chid = int(input('请输入你要修改记录的编号:'))
        cursor = conn.cursor()
        mylist = cursor.execute('select * from family where id=(?)', (chid,))
        for row in mylist:
            print('1编号：', row[0], end=' ')
            print('2姓名：', row[1], end=' ')
            print('3电话：', row[2], end=' ')
            print('4地址：', row[3])
        chnum = int(input('请输入你要修改的项的编号:'))
        if chnum == 1:
            # 修改编号
            newid = int(input('请输入修改后的编号:'))
            cursor.execute('update family set id=? where id=?', (newid, chid))
        elif chnum == 2:
            # 修改姓名
            newname = input('请输入修改后的姓名:')
            cursor.execute('update family set name=? where id=?', (newname, chid))
        elif chnum == 3:
            # 修改电话
            newtele = input('请输入修改后的姓名:')
            cursor.execute('update family set tele=? where id=?', (newtele, chid))
        elif chnum == 4:
            # 修改地址
            newaddress = input('请输入修改后的姓名:')
            cursor.execute('update family set address=? where id=?', (newaddress, chid))
        conn.commit()
        cursor.close()
        print('修改数据成功')
    elif choice == 5:
        chid = int(input('请输入你要删除记录的编号:'))
        cursor = conn.cursor()
        mylist = cursor.execute('select * from family where id=(?)', (chid,))
        for row in mylist:
            print('编号：', row[0], end=' ')
            print('姓名：', row[1], end=' ')
            print('电话：', row[2], end=' ')
            print('地址：', row[3])
        chok = input('你确定要删除吗?（y/n）:')
        if chok == 'y' or chok == 'Y':
            cursor.execute('delete from family where id=?', (chid,))
            print('删除成功')
        else:
            print('你已取消删除操作!')
        conn.commit()
        cursor.close()
    elif choice == 6:
        print('1编号：', end=' ')
        print('2姓名：', end=' ')
        print('3电话：', end=' ')
        print('4地址：', )
        chnum = int(input('请输入排序所依据的项的编号:'))
        cursor = conn.cursor()
        if chnum == 1:
            mylist = cursor.execute('select * from family order by id desc')
        elif chnum == 2:
            mylist = cursor.execute('select * from family order by name')
        elif chnum == 3:
            mylist = cursor.execute('select * from family order by tele')
        elif chnum == 4:
            mylist = cursor.execute('select * from family order by address')
        for row in mylist:
            print('编号：', row[0], end=' ')
            print('姓名：', row[1], end=' ')
            print('电话：', row[2], end=' ')
            print('地址：', row[3])
        print('数据表排序完成')
        cursor.close()
conn.close()