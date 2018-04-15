

# list1=[1,2,3,4,5,6,7]
# list1[0:-1]      #最后一个不取
# list1[1::2]       #取偶数位
# list2=['a','b']
# list1.extend(list2)

# for i in list1:
#     list2.append(i)


# list1.count()


# #元祖的查询效率高
# touple=('hell0',)     #定义一个元祖
# touple.count()
# touple.index()

# list(touple)     #list和touple相互转换
# touple(list1)

# dict={'A':'b','B':'b'}

# dict.popitem()  
# dict.values()


# #斐波那契数列

# x=1
# y=1
# for i in range(1,20):
#     x,y=y,x+y
# print(y)
    

# q=1
# w=1
# i=1
# while w<6000 :
#     q,w=w,q+w 
#     i+=1
# print(i,w)

# sum=0
# list3=[1,2,7,4]
# for i in  list3:
#     for j in  list3:
#         for k in  list3:
#             for w  in  list3:
#                 if i!=j and i!=k and i!=w and j!=k and j!=w and k!=w:
#                     print(i*1000+j*100+k*10+w)
#                     sum+=1
# print(sum)


#生成一个奇数的列表
list1=[]
for i in range(1,11):
 if i/2-int(i/2)!=0:
     list1.append(i)
print(list1)

list6=[o for o in range(1,10,2)]
print(list6)


