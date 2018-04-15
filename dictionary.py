x={"A":'a',"B": 'b','C': 'c','D': 'd','E':'e','F':'f','G':'g','H':'h','I':'i','J':'j','K':'k','L':'l','M':'m','N':'n','O':'o',
'P':'p','Q':'q','R':'r','S':'s','T':'t','U':'u','V':'v','W':'w','X':'x','Y':'y','Z':'z'}
# print(x.values())
# i=str(x)
# print(i)
print(x['A'])       #输入A对应的值

# x={"A":1,"B":2,"C":3}
# print(x)
# x.keys()  #找到所以的key
# x.items()  #找到所有的元素，输出由元祖（每对值）组成的列表
# x.values()   #找到所有的值
# x.get('AI')
# x.clear()   #清空
# x.copy()    #完全复制
# len(x)      #统计长度
# str(x)      #字典转换为字符串
# del(x)      #删除
# print('C' in x)     #判断C是否在字典x中

# dict1=x.fromkeys([1,2,3],[2,3,4])       #第一个元素和第二个元素遍历组合生成一个字典,前面的一个序列是 key,
# print(dict1)

# xiaomin={"inteilgant":"智能的","AI":"人工智能","youdao":"有道","apple":"苹果x","factory":"富土康"}
# # print(xiaomin.keys())
# # print(xiaomin.values())
# # print(xiaomin.items())
# # dict1=xiaomin.copy()
# # # dict2=xiaomin.fromkeys([1,2,3],[2,3,4])
# # dict1.popitem()   #随机删除
# # print(dict1)

# xiaomin["factory"]='富士康'     #改变factory对应的值
# print(xiaomin)

# xiaomin={"inteilgant":"智能的","AI":"人工智能","youdao":"有道","apple":"苹果7","apple":"苹果x","factory":"富土康"}
# print(xiaomin['apple'])     #key相同时，后面的值会把前面的值覆盖

#xiao={1:'q','st':'kkk',(1,2,3):(2,3,4),[1,2,3]:[2,3,4]}    #字典中key必须不可变，所有可以用数字，字符串，元祖来充当，但是列表不可以
xia1={"inteilgant":"智能的","AI":"人工智能","youdao":"有道","apple":"苹果7","apple":"苹果x","factory":"富土康"}
print(len(xia1)) 
print(str(xia1))
xia1.pop("AI")     #删除AI，使用pop方法，里面必须要有参数
#del(xia1['AI'])    #删除AI
print(xia1)

