class Foo:
    animal='兔子'
    def __init__(self,feature):
        self.feature=feature
    def print(self):
        print('调用了实例方法')
        print('{0}的特征是：{1}'.format(self.animal,self.feature))
    @classmethod
    def enemy(cls,name):
        print('调用了类方法')
        enemyName=name
        print('{0}的天敌是：{1}'.format(cls.animal,enemyName))
    @staticmethod
    def eat(name):
        print('调用了静态方法')
        eatName = name
        print('{0}的食物是：{1}'.format(Foo.animal, eatName))
if __name__=='__main__':
    t=Foo(['长耳朵','三瓣嘴','两颗大门牙','毛柔软','红眼睛'])
    t.print()
    t.enemy(['狼','老鼠'])
    Foo.enemy(['黄鼠狼','狐狸'])
    t.eat(['青草','胡萝卜','白菜','薯类'])
    Foo.eat(['苹果', '南瓜', '蒲公英', '车前草'])