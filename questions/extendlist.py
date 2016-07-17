#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

def extendList(val,list=[]):
    list.append(val)
    return list

list1=extendList(10)
list2=extendList(123,[])
list3=extendList('a')

print ("list1 = %s" % list1)
print ("list2 = %s" % list2)
print ("list3 = %s" % list3)

'''
新的默认列表仅仅只在函数被定义时创建一次。随后当 extendList 没有被指定的列表参数调用的时候，其使用的是同一个列表。这就是为什么当函数被定义的时候，表达式是用默认参数被计算，而不是它被调用的时候.
list1 和 list3 是操作的相同的列表。而 ````list2是操作的它创建的独立的列表（通过传递它自己的空列表作为list``` 参数的值）。
'''

#改进方式：
#当没有新的 list 参数被指定的时候，会总是开始一个新列表，这更加可能是一直期望的行为。

def extendList(val,list=None):
    if list is None:
        list=[]
    list.append(val)
    return list

list1=extendList(10)
list2=extendList(123,[])
list3=extendList('a')


print ("list1 = %s" % list1)
print ("list2 = %s" % list2)
print ("list3 = %s" % list3)




