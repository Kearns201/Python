class fruit:
    name='apple'
    price=6.7
    def printName(self):
        print(self.name)
        print(self.price)
if __name__=='__main__':
    myfruit=fruit()
    myfruit.printName()
    print('fruit.name={0},fruit.price={1}'.format(fruit.name, fruit.price))
    myfruit.name='pear'
    myfruit.price=3.5
    myfruit.printName()
    print('fruit.name={0},fruit.price={1}'.format(fruit.name,fruit.price))
