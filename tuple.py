# tuple1=('A','a','B','b','C','c','D','d')    #tuple和list的区别，一个使用[],一个是小括号（）
# tuple2=('A','a','B','b')
# tuple3=tuple1+tuple2             #tuple本身不可以被改变，本身没有方法，所有不支持 expend，pop，append，仅支持查询，切片



#tuple4=(1,2,4,5,6,[3,4,6])     #元组本身不可被更改，但是元祖中的可变类型的元素（列表，字符串）可以被更改
#将tuple4转化成下面的元祖
#tuplex=(1,2,4,5,6,[2,4,6])
# tuple4[5][0]=2
# print(tuple4)

tuple5=(1,2,4,5,6,'wueueiiriir')
a=tuple5[5].capitalize()
print(a)


tuple1=(5,)     #定义元祖时，仅有一个元素时，不要忘记加逗号
print(type(tuple1))
