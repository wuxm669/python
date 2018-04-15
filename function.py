
# def hello2(a):       #括号内的值，就相当于传的参数
#     print('hello'*a)
# hello2(5)

# def hello3(a,b):
#  if a*b/2 >10:
#     return '大三角形'
#  elif (a*b/2)<11:
#     return '小三角形'
#  else:
#     return '输入不合法'
            
# print(hello3(3,2))      #重复输出时，会导致输出为None

#return 返回的类型，就相当于调用这个函数时，函数的类型

# a=[1,2]
# def add1(a):
#     a.append('E')
# add1(a)
# print(a)

# def hello4(a,b,c):
#     print(a*b*c)

# hello4(1,2,3)

# def printinfo(arg1,*vartuple):
#     print('输出：')
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return

# printinfo(10)
# printinfo(70,60,50)

#函数自己调用自己
# def f(a):
#     if a==1:
#        return 1
#     elif a!=1:
#        return(a+f(a-1))    #return 返回的类型，就相当于调用这个函数时，函数的类型
# i=1
# while f(i)<6000:
#     i+=1
# print(i-1)


# #第二天是第一天的1倍，99天的时候，开了一半，则什么时候开满

# def k(i):
#  if i==1:
#     return 1
#  else :
#     return 2*k(i-1)


# #匿名函数
# #lambda [arg1 [,arg2,.....argn]]:expression
# a=lambda x,y:x*x+5+1+y
# print(a(2,3))



#作用域链
 
name = "lzl"
def f1():
    name = "Eric"
    print(name)
    def f2():
        name = "Snor"
        print(name)
    f2()
f1()
print(name)

#Eric    Snor    lzl

# name = "lzl"
# def f1():
#     print(name)
 
# def f2():
#     name = "eric"
#     print(name)
#     f1()

# f2()          #执行结果：eric   ，lzl

# def outer():
#     num=10
#     def inner():
#         nonlocal num    #关键字声明将全局变量变为内部变量
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()

num=1
def fun1():
    global num
    print(num)
    num=123
    print(num)
fun1()



#递归
# 1.初始值得定义清楚   f1=1...或者 f0=... 
# 2、n和n-1或者n-2有关系，且变量逐渐变小


li = [lambda :x for x in range(10)]
#li = [i for i in lambda :x for x in range(10)]
li2=[x for x in range(10)]
print(li)
print(li2)