# # 声明一个Employee 类
# class Employee:
#     # 声明一个类的变量
#     pay_raist_amount = 1.2

#     __weight = 40    #私有变量
#     # 创建一个构造器
#     def __init__(self,first,last,pay,weight,domain="funcat.com"):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first+last+"@"+domain
#         self.__weight = weight
#     def say(self):
#         print("{}".format(self.__weight))
#     # 创建一个方法
#     def __say(self):     #私有方法，外部不能直接被调用，要是想调用，只能通过一个非私有方法去包装一下再去调用
#         print("helloworld {}".format(self.__weight))

#     def Isay(self):
#         self.__say()

#     def fullname(self):
#         return '{}-{}-{}'.format(self.first,self.last,self.pay)

#     def new_pay0(self):
#         # return self.pay * Employee.pay_raist_amount
#         return self.pay * self.pay_raist_amount

# #私变变量，只能在内部使用，不能再外部使用或更改，私有变量一般是在创建构造器的时候赋值或更改
# #私有方法，外部不能直接被调用，要是想调用，只能通过一个非私有方法去包装一下再去调用
# # 创建一个类的实例
# emp1 = Employee("xiaoming","wang",10000,50,"baidu.com")
# emp1.__weight = 60     #私有变量，在外部不能被更改
# emp1.say()
# # emp2 = Employee("xiaohong",'zhang',20000)
# # print(emp1.fullname())
# emp1.Isay()


class People:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name =n
        self.age =a
        self.__weight = w
    def speak(self):
        print('%s 说:我 %d 岁了'%(self.name,self.age))

class Student(People):
    
    def __init__(self,n,a,w,grade):
        People.__init__(self,n,a,w)     #父类定义过的变量，子类可以不用重复定义
        #super().__init__(n,a,w)     #第二种方法
        self.grade = grade
    # 方法重写
    def speak(self):
        print("%s 说: 我 %d岁, %d 年级" %(self.name,self.age,self.grade))


s = Student('xiaoming',20,50,5)
s.speak()

class Teacher(Student,People):
    pass
