import random

print("扑克游戏发牌模拟")
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
suits = ('黑桃', '红桃', '方块', '梅花')
puke = [(x, y) for x in suits for y in ranks]
pai = puke * 2
cardRand = random.sample(pai, 104)
play1 = []
play2 = []
play3 = []
play4 = []
for i in range(26):
    play1.append(cardRand.pop())
    play2.append(cardRand.pop())
    play3.append(cardRand.pop())
    play4.append(cardRand.pop())
play1.sort(key=lambda x: x[0])
play2.sort(key=lambda x: x[0])
play3.sort(key=lambda x: x[0])
play4.sort(key=lambda x: x[0])
print("玩家1的牌：")
i = 1
for each in play1:
    print(each, end=',')
    if i % 6 == 0:
        print()
    i = i + 1
print("\n玩家2的牌：")
i = 1
for each in play2:
    print(each, end=',')
    if i % 6 == 0:
        print()
    i = i + 1
print("\n玩家3的牌：")
i = 1
for each in play3:
    print(each, end=',')
    if i % 6 == 0:
        print()
    i = i + 1
print("\n玩家4的牌：")
i = 1
for each in play4:
    print(each, end=',')
    if i % 6 == 0:
        print()
    i = i + 1
