
#list的存放机制，先到后得      请对比tuple一起学习
#切片后面都跟中括号[]，下标也是中括号[]

# list1=['A','a','B','b','C','c','D','d']
# X=input('......')
# print(X in list1 )        #判断字符是否在list中
# list2=list1[0::2]         #步长为2取偶数位
# list3=list1[7::-2]        #反向取步长为2取奇数位
# # list3=list1[1::2] 
# # list3.reverse()    #reverse 反向显示
# print(list2)
# print(list3)
# list2.extend(list3)  #  extend如果是两个列表的拼接，将list3中的元素拼接到list2上，只能两个list进行拼接
# # for i in list2:
# #     list1.append.list2[i]
# print(list2)
# list2.append(list3)   #直接将列表list3当做一个元素插入
# print(list2)
# append和extend都仅只可以接收一个参数，这是为什么下面传入多个参数会报错的原因
# append 直接把要添加的东西，当做一个元素插入
# extend 只能是一个列表

# print(list1)
# print(type(list1))      #输入List的类型
# print(type(list1[0]))   #输入第一个值的类型
# print(list1[1:3])       #切片时，右边的值取不到
# print(list1[1:])        #取第一个到最后一个
# print(list1[0:-1])      #取到倒数倒数第二个
#print（list1[-8:-1]）

# print(list1.count('A'))   #count 查看有多少个A
# print(list1.index('b'))   #index  寻找b的位置
# print(list2+list3)       #+ 两个数组添加
# list1.append("E")        #append 末尾添加
# list1.insert(1,"X")      #insert 指定位置添加
# print(list1)
# list1.pop(0)              #pop 指定删除第一位，为空则删除最后一位
#list1.remove(2)            #remove （）中写要删除的元素本身，不是下标 即删除列表中第一次出现的2
#list2=list1.copy()        #copy
#list2.clear()                          #clear 清空列表
# #del list2               #将list2删除
#list2.index('C')      #index 查看c在list2中第一次出现的位置，即索引

#list去重    3种方法
# count()  
# in 判断是否在列表中，在就不要，不在就append添加
#set()                #去重复
#乘法  list5*3       #* 直接显示3个list5相加的列表

list5=[1,2,3,4,5,6,1,2,4,4]
list6=[]
for i in list5:          #i是for中自己定义的变量，不用给值，默认按照list中的下标循环   #第一个for应该左对齐
    if i not in list6:
        list6.append(i)
print(list6)
# list5.sort()       #永久修改排序，并将结果报错至list5
# print(list5)
#print(sorted(list5))    #临时排序但是不会改变list5


import copy
 
a = [1, 2, ['a', 'b']]
b = copy.copy(a)      #copy：浅拷贝。只拷贝父对象，不会拷贝对象的内部的子对象
c = copy.deepcopy(a)   #deepcopy：深拷贝。拷贝对象及其子对象
 
a.append(3) 
a[2].append('c')
print(a,'\n',b,'\n',c,'\n')

# —–我们寻常意义的复制就是深复制，即将被复制对象完全再复制
# 一遍作为独立的新个体单独存在。所以改变原有被复制对象不会对已经复制出来的新对象产生影响。 
# —–而浅复制并不会产生一个独立的对象单独存在，他只是将原有的数据块打上一个新标签，
# 所以当其中一个标签被改变的时候，数据块就会发生变化，另一个标签也会随之改变。这就和我们寻常意义上的复制有所不同了。
# 对于简单的 object，用 shallow copy 和 deep copy 没区别
# 复杂的 object， 如 list 中套着 list 的情况，shallow copy 中的 
# 子list，并未从原 object 真的「独立」出来。也就是说，如果你改变原 object 的子 
# list 中的一个元素，你的 copy 就会跟着一起变。这跟我们直觉上对「复制」的理解不同。




# json.dumps()       #jsion相关的操作
# json.loads()

