# #!/usr/bin/python2.7
# # -*- coding: utf-8 -*-
# import array
# #array模块是python中实现的一种高效的数组存储类型。它和list相似，但是所有的数组成员必须是同一种类型，在创建数组的时候，就确定了数组的类型

# #array.array(typecode,[initializer]) --typecode:元素类型代码；initializer:初始化器，若数组为空，则省略初始化器
# arr = array.array('i',[0,1,1,3])
# print(arr)

# #array.typecodes --模块属性
# print('\n输出一条 包含所有可用类型代码的字符串：')
# # print(array.typecodes) #注意调用者是模块名，不是某个对象

# #array.typecode -- 对象属性
# print('\n 输出 用于创建数组的类型代码字符：')
# print(arr.typecode)

# #array.itemsize --对象属性
# print('\n输出 数组的元素个数：')
# print(arr.itemsize)

# #array.append(x) --对象方法
# print('\n将一个新值附加到数组的末尾：')
# arr.append(4)
# print(arr)

# #array.buffer_info() -- 对象方法
# print('\n获取数组在存储器中的地址、元素的个数，以元组形式（地址、长度）返回：')
# print(arr.buffer_info())

# #array.count(x) -- 对象方法
# print('\n获取元素1在数组中出现的次数：')
# print(arr.count(1))

# #array.extend(iterable) -- 对象方法：将可迭代对象的袁旭序列附加到数组的末尾，合并两个序列
# print('\n将可迭代对象的元素序列附加到数据的末尾，合并两个序列：')
# #注意：附加元素数值类型必须与调用对象的元素的数值类型一致
# _list = [5,6,7]
# arr.extend(_list)
# print(arr)

# #array.fromlist(list) --对象方法：将列表中的元素追加到数组后面，相当于for x in list:a.append(x)
# print('\n将列表中的元素追加到数组后面，相当于for x in list:a.append(x):')
# arr.fromlist(_list)
# print(arr)

# #array.index(x) --对象方法：返回数组中x的最小下标
# print('\n返回数组中1的最小下标：')
# print(arr.index(1))

# #array.insert(1) --对象方法：在下表i（负值表示倒数）之前插入值x
# print('\n在下表1（负值表示倒数）之前插入值0：')
# arr.insert(1,0)
# print(arr)

# #array.pop(i) --对象方法：删除索引为i的项，并返回它
# print('\n删除索引为4的项，并返回它:')
# print(arr.pop(4))
# print(arr)

# #array.remove(x) --对象方法：删除第一次出现的元素x
# print('\n删除第一次出现的元素5：')
# arr.remove(5)
# print(arr)

# #array.reverse() --对象方法：反转数组中的元素值
# print('\n将数组arr中元素的顺序反转：')
# arr.reverse()
# print(arr)

# #array.tolist()：将数组转换为具有相同元素的列表（list）
# print('\n将数组arr转换为已给具有相同元素的列表：')
# li = arr.tolist()
# print(li)







# #include<cstdio>
# #define ts(x) #x
# char str[]=ts(
# int main(){
# puts(ts(#include<cstdio>));puts(ts(#define ts(x) #x));printf(ts(char str[]=ts(%s);),str);puts(ts());puts(str);});

# int main(){
# puts(ts(#include<cstdio>));
# puts(ts(#define ts(x) #x));
# 	printf(ts(char str[]=ts(%s);),str);
# 	puts(ts());
# 	puts(str);}
# 	
# import re
# a = 'Mozilla/5.0 (Linux; Android 4.4.4; Coolpad Y82-520 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.5.4.1000 NetType/4G Language/zh_CN'
# b = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Mobile/14D27 MicroMessenger/6.5.5 NetType/WIFI Language/zh_CN'
# ss = re.findall(r"iPhone",a)
# print ss


def findWords(words):
    a = {'q','w','e','r','t','y','u','i','o','p'}
    print(a)
    b = {"a","s","d","f","g","h","j","k","l"}
    c = {"z","x","c","v","b","n","m"}
    ret = []
    for i in words:
        j = set(i.lower())
        if j <= b:
            ret.append(i)
    print(ret)


words = ["Hello", "Alaska", "Dad", "Peace"]
findWords(words)
