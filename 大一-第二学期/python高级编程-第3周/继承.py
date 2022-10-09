class Person:
    __countPerson=0   
    def __init__(self, name, age):   
        self.name = name   
        self.age = age
        Person.__countPerson=Person.__countPerson+1 
        self.__countPrint()  
    def out(self):   
        print('Name:{0},Age:{1}'.format(self.name, self.age))
    def eat(self,cook):
        print('I am eating {0}'.format(cook))
    @classmethod
    def __countPrint(cls):
        print('Person的构造函数，人数:{0}' .format(Person.__countPerson)) 
             
class Student(Person): 
    __countStudent=0  
    def __init__(self, name, age, grades):   
        Person.__init__(self, name, age)   
        self.grades = grades 
        Student.__countStudent=Student.__countStudent+1   
        self.__countPrint()  
    def out(self):   
        Person.out(self)   
        print('成绩为:{0}'.format( self.grades)) 
    def study(self,course): 
        print('我正在学习{0}课程'.format(course))
    @classmethod
    def __countPrint(cls):
        print('Student的构造函数:学生人数为{0}'.format(Student.__countStudent))  

class Teacher(Person):
    __countTeacher=0   
    def __init__(self, name, age, salary):   
        Person.__init__(self, name, age)   
        self.salary = salary 
        Teacher.__countTeacher=Teacher.__countTeacher+1 
        self.__countPrint()            
    def out(self):   
        Person.out(self)   
        print('工资为:{0}'.format(self.salary))
    def work(self,course): 
        print('我正在教授{0}课程'.format(course))
    @classmethod
    def __countPrint(cls):
        print('Teacher的构造函数:老师人数为{0}'.format(Teacher.__countTeacher)) 
if __name__ == '__main__': 
    s = Student('张明', 19, [80,90,77])   
    t = Teacher('刘华', 35, 8000)   
    s.out()
    s.study(['Python','数据结构','计算机原理'])
    s.eat('蛋炒饭')
    t.out()
    t.work('Python')
    t.eat('包子')
    print(issubclass(Student,Person)) 
    print("Person的父类:",Person.__bases__)  
    print("Teacher的父类:",Teacher.__bases__)
    print(isinstance(t,Teacher))
    print("s对象的类是:",s.__class__)     
    s.__countPrint()
    
    
