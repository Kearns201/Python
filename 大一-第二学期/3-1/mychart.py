import csv
import copy


class Cart:
    def __init__(self):
        self.__mycart = []

    def addGoods(self, goods):
        self.__mycart.append(goods)

    def deleteAllGoods(self):
        self.__mycart.clear()

    def displayCart(self):
        print(self.__mycart)


if __name__ == '__main__':
    with open('data\goodinfo.csv', 'r') as goodsfile:
        goodsList = []
        lines = csv.reader(goodsfile)
        for line in lines:
            goodsList.append(line)
            for item in line:
                print('{:<12}\t'.format(item), end='')
            print()
    mycart = Cart()
    while True:
        buy = input('你要购买商品吗？(y/n)')
        if buy == 'y':
            goodid = input('请输入商品的编号：')
            goodnum = int(input('请输入商品的数量：'))
            for good in goodsList:
                if good[0] == goodid:
                    if goodnum >= 1 and goodnum <= int(good[3]):
                        temp = copy.copy(good)
                        temp[3] = int(temp[3]) - goodnum
                        temp.append(goodnum)
                        if goodnum > 2:
                            total = goodnum * float(temp[4]) * float(temp[5])
                        else:
                            total = goodnum * float(temp[4])
                        temp.append(total)
                        mycart.addGoods(temp)
                        mycart.displayCart()
                    else:
                        print('输入的商品数量无效')
                    break
            else:
                print('商品编号输入错误')
        else:
            break

        mycart = Cart()
        mycart.addGoods('ipad')
        mycart.addGoods('手机')
        mycart.displayCart()
        mycart.deleteAllGoods()
        mycart.displayCart()
