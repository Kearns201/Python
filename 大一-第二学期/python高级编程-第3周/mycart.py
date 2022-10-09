import os
import csv
import copy


class Cart:

    def __init__(self):
        self.__myCart = []

    def addGoods(self, goods):
        if len(self.__myCart) != 0:
            for item in self.__myCart:
                if goods[0] == item[0]:
                    item[3] = goods[3]
                    item[6] = item[6] + goods[6]
                    if (item[6] >= 5):
                        item[7] = float(item[4]) * float(item[5]) * int(item[6])
                    else:
                        item[7] = float(item[4]) * int(item[6])
                    break;
            else:
                self.__myCart.append(goods)
        else:
            self.__myCart.append(goods)
        print('购物车', self.__myCart)

    def displayCart(self):
        print(self.__myCart)
        print('您的购物车'.center(80, '#'))
        print('%-5s \t %-14s \t %-8s \t %-8s \t %-8s \t %-8s' \
              % ('商品编号', '商品名称', '商品价格(元)', '折扣（5件以上）', \
                 '购买数量(个)', '购买金额（元）'))
        totalNum = 0
        totalAmount = 0
        for t in self.__myCart:
            print('%-10s \t %-14s \t %-8s \t %-8s \t %-8.2f\t %-8.2f' \
                  % (t[0], t[1], t[4], t[5], t[6], t[7]))
            totalNum = totalNum + t[6]
            totalAmount = totalAmount + t[7]
        print('合计：总数量为：{0}，总价为{1}'.format(totalNum, totalAmount))

    def modifyGoods(self, goodid, goodnum):
        if len(self.__myCart) != 0:
            for item in self.__myCart:
                if goodid == item[0]:
                    item[6] = goodnum
                    if (item[6] >= 5):
                        item[7] = float(item[4]) * float(item[5]) * int(item[6])
                    else:
                        item[7] = float(item[4]) * int(item[6])
                    print('成功修改')
                    break;
            else:
                print('购物车中无该类商品！')

    def deleteGoods(self, goodid):
        if len(self.__myCart) != 0:
            for item in self.__myCart:
                if goodid == item[0]:
                    self.__myCart.remove(item)
                    print('成功删除')
                    break;
            else:
                print('购物车中无该类商品！')

    def deleteAllGoods(self):
        if len(self.__myCart) != 0:
            self.__myCart.clear()
            print('购物车中无任何商品！')

    def openUserCart(self):
        fileName = input('请输入要打开文件的路径和文件名')
        # 使用open()函数打开用户输入的文件，如果不存在这个文件，则报错
        with open(fileName, 'r') as mycsvFile:
            # 使用reader函数读入整个csv文件到一个列表对象中  
            self.__myCart.clear()
            lines = csv.reader(mycsvFile)
            for line in lines:
                # 输出csv文件当前行  
                self.__myCart.append(line)
            for item in self.__myCart:
                item[6] = float(item[6])
                item[7] = float(item[7])
            print('打开文件成功！')

    def saveUserCart(self):
        fileName = input('请输入要保存的文件的路径和文件名')
        with open(fileName, 'w', newline="") as mycsvFile:
            # 创建csv文件写对象      
            myWriter = csv.writer(mycsvFile)
            # 调用writerows函数一次写入一个列表
            myWriter.writerows(self.__myCart)
            print('保存文件成功！')


def main():
    file = r'data/goodinfo.csv'
    goodList = []
    titleList = []
    with open(file, 'r') as csvfile:
        lines = csv.reader(csvfile)
        for line in lines:
            if line != []:
                goodList.append(line)
        titleList = goodList[0]
        goodList = goodList[1:]
    userCart = Cart()
    print("简单的购物车模拟程序")
    while (True):
        print('{:<14}'.format('1.添加商品到购物车'), end='  ')
        print('{:<14}'.format('2.修改购物车'), end='  ')
        print('{:<14}'.format('3.删除购物车中商品'), end='  ')
        print('{:<14}'.format('4.展示购物车中商品'))
        print('{:<14}'.format('5.清空购物车'), end='  ')
        print('{:<14}'.format('6.打开已存在购物车'), end='  ')
        print('{:<14}'.format('7.保存购物车'), end='  ')
        print('{:<14}'.format('0.退出购物'))
        choice = int(input('请输入您的选择（0-7）'))
        if choice == 0:
            exit(0)
        elif choice == 1:
            while True:
                print('欢迎来到购物商城，请选择商品')
                for each in titleList:
                    print('{0:<12}\t'.format(each), end='')
                print()
                for item in goodList:
                    for each in item:
                        print('{0:<12}\t'.format(each), end='')
                    print()
                buy = input('是否继续购物？（Y/N）')
                if (buy == 'y' or buy == 'Y'):
                    goodid = input('请输入商品编号：')
                    goodnum = int(input('请输入要购买的商品数量：'))
                    for item in goodList:
                        if goodid == item[0]:
                            if (goodnum >= 0 and goodnum <= int(item[3])):
                                print('item=', item)
                                item[3] = str(int(item[3]) - goodnum)
                                tmp = copy.copy(item)
                                tmp.append(goodnum)
                                if (tmp[6] >= 5):
                                    total = float(tmp[4]) * float(tmp[5]) * int(tmp[6])
                                else:
                                    total = float(tmp[4]) * int(tmp[6])
                                tmp.append(total)
                                userCart.addGoods(tmp)
                                break;
                            else:
                                print('购买数量有误，请重新输入')
                                break;
                    else:
                        print('商品编号输入错误，请重新购物')
                else:
                    break;
        elif choice == 2:
            print('####修改购物车中商品数量#####')
            goodid = input('请输入商品编号：')
            goodnum = int(input('请输入要购买的商品数量：'))
            for item in goodList:
                if goodid == item[0]:
                    if (goodnum >= 0 and goodnum <= int(item[3])):
                        userCart.modifyGoods(goodid, goodnum)
                    else:
                        print('购买数量有误，请重新输入')
                    break;
            else:
                print('商品编号输入错误')

        elif choice == 3:
            print('####删除购物车中商品#####')
            goodid = input('请输入商品编号：')
            for item in goodList:
                if goodid == item[0]:
                    userCart.deleteGoods(goodid)
                    break;
            else:
                print('商品编号输入错误')

        elif choice == 4:
            userCart.displayCart()
        elif choice == 5:
            userCart.deleteAllGoods()
        elif choice == 6:
            userCart.openUserCart()
        elif choice == 7:
            userCart.saveUserCart()
        else:
            print('输入有误，请重新输入！')


main()
