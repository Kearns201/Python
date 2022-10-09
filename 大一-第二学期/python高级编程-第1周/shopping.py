goods = {'01': ['牛奶', 1.5], '02': ['橙汁', 5.8], '03': ['酸奶', 2.5],
         '04': ['啤酒', 5.5], '11': ['牙膏', 6.8], '12': ['牙刷', 4.6],
         '13': ['洗发水', 22.5], '14': ['沐浴液', 27], '21': ['上衣', 155],
         '22': ['牛仔裤', 215], '23': ['帽子', 55], '24': ['袜子', 12.3],
         '31': ['火腿', 23], '32': ['培根',21 ], '33': ['酱肉', 45],
         '34': ['牛肉', 65]}
user1 = [['01', 20], ['02', 4], ['04', 6], ['13', 1], ['31', 1]]
user2 = [['01', 15], ['03', 4], ['11', 1], ['12', 3], ['22', 1], ['23', 2], ['31', 1], ['33', 2]]
user3 = [['01', 10], ['02', 3], ['03', 6], ['13', 1], ['31', 1], ['32', 3]]
set1 = set()
set2 = set()
set3 = set()
total = 0
for item in user1:
    tmp = goods.get(item[0])
    total = total + tmp[1] * item[1]
    set1.add(item[0])
print('第一个客户的购物总额是:{0}'.format(total))
total = 0
for item in user2:
    tmp = goods.get(item[0])
    total = total + tmp[1] * item[1]
    set2.add(item[0])
print('第二个客户的购物总额是:{0}'.format(total))
total = 0
for item in user3:
    tmp = goods.get(item[0])
    total = total + tmp[1] * item[1]
    set3.add(item[0])
print('第三个客户的购物总额是:{0}'.format(total))
set4 = set1 | set2 | set3
set5 = set1 & set2 & set3
setall = set(goods.keys())
set6 = setall - set4
print('有人购买的商品有：{0}'.format(set4))
print('所有人都购买的商品有：{0}'.format(set5))
print('无人购买的商品有：{0}'.format(set6))
