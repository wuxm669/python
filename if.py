#输入10以内的奇数
# for x in range(1,11,2) 
# while     
# 标识符的三个命名规范        1,字母或下划线开头，2,区分大小写 3,字母、数字和下划线组成
# str.capitalize()     将首字母大写，其余字母小写


# 输入成绩判断
# score=int(input("请输入成绩....."))
# if score>0 and score<101:
#     if score>=80:
#         print('good')
#     elif score>=60:
#         print('just so so')
#     else:
#         print('bad')
# else :
#      print('error')


#九九乘法表
# import math 
# for x in range(1,10) :
#   for y in range(1,x+1) :
#     sum=x*y
#     print(y,'*',x,'=',y*x,end='  ')     #以空格结尾
#   print("  ")



#有1、3、5、7 四个数字组成四位数，能组成多少互不相同且无重复数字的四位数？都是多少？  i,j,k,l
# sum=0
# for i in range(1,9,2):   #1-9的整数，间隔是2
#     for j in range(1,9,2):
#         for k in range(1,9,2):
#             for l in range(1,9,2):
#                 if i!=j and i!=l and i!=k and j!=k and j!=l and k!=l:
#                     print(i*1000+j*100+k*10+l)
#                     sum+=1
# print(sum)


# break   中断当前的循环，一般与if 一起用
# continue   继续
# pass     跳过
#当输入的值为5时，跳出循环
#a=int(input("请输入1-10的整数。。。"))
# i=0
# while i<11 :
#     i+= 1
#     if i!=5:
#         print("此时输入的数字不是5")
#         print(i)
#         continue
         

# list1=[1,2,3,4,5,6,7]
# for a in list1


#题目 一个整数，它加上100后是一个完全平方数，加上168也是一个完全平方数，请问这个数是多少？
# from math import sqrt
# x=0
# while x>=0:
#     if sqrt(x+100)-int(sqrt(x+100))==0 and sqrt(x+168)-int(sqrt(x+168))==0:
#        print(x)
#        break
#     x+=1

#斐波那契数列    i等于前两个值相加
i=1
j=1
z=0
while i<2000:
    i,j=j,j+i
    z+=1
    print(i)