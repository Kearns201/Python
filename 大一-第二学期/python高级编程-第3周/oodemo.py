class Foo:
    animal = '兔子'

    def __init__(self, feature):
        self.feature = feature

    def print(self):
        print('调用了实例方法')
        print('{0}的特征是：{1}'.format(self.animal, self.feature))

    @classmethod
    def enemy(cls, name):
        print('调用了类方法')
        enemyName = name
        print('{0}的天敌是：{1}'.format(cls.animal, enemyName))

    @staticmethod
    def eat(name):
        print('调用了静态方法')
        eatName = name
        print('{0}的食物是：{1}'.format(Foo.animal, eatName))
