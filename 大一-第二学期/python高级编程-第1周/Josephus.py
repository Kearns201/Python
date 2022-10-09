num = int(input("请输入参与的人数:"))
if num <= 0:
    print("输入错误！")
    exit(0)
name=[]
for i in range(num):
    name.append(input("请输入第{0}个人的名字：".format(i+1)))
k = int(input("请输入k:"))
Q=[]
for each in name:
    Q.append(each)
while len(Q)>=1:
    for i in range(k-1):
        Q.append(Q.pop(0))
    print(Q.pop(0))
