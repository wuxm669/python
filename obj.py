# a = 1
# b = 1  
# c = a+b
# d =a-b
# def add(x,y):
#     print(x+y)
#     return x+y
# add(1,2)

#声明一个employee类
class Employee:
    pay_raist_amount=1.2
    #创建一个构造器
    def __init__(self,first,last,pay,domin="ersoft.cn"):
        self.first =first
        self.last =last
        self.pay =pay
        self.email =last+first+'@'+domin

    #创建一个方法
    def fullname(self):
        #print('{} {}'.format(self.last,self.first) )  #大括号的使用方法
        return self.first + self.last
    def new_pay0(self):
        return self.pay*self.pay_raist_amount      #引用方法本身的变量（实际用这种方法比较多）
    def new_pay1(self):
        return self.pay*Employee.pay_raist_amount   #引用的全局变量
#实例化
emp1 =Employee('xiaoming','wang',1000)  
emp1.fullname()
emp2 =Employee('xiaohong','zhang',2000)
print(emp1.first,emp1.last,emp1.pay,emp1.email)
#调用一个方法
print(emp1.new_pay0())
print(emp1.new_pay1())
Employee.pay_raist_amount = 1.4
print('Employee.pay_raist_amount = 1.4',emp1.new_pay0())
print(emp1.new_pay1())
print(emp2.new_pay0())
print(emp2.new_pay1())
emp1.pay_raist_amount = 1.5
print("emp1. raise, emp1.newpay0()",emp1.new_pay0())
print(emp1.new_pay1())
print(emp2.new_pay0())
print(emp2.new_pay1())
emp2.pay_raist_amount = 1.6
print('emp2. raise, emp2.newpay0()',emp1.new_pay0())
print(emp1.new_pay1())
print(emp2.new_pay0())
print(emp2.new_pay1())

