#!/usr/bin/env python3 

#-*-coding:utf-8 -*-


#itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。

import itertools 

#count will add 1 value for each time 
naturals=itertools.count(2)
for n in naturals:
    if n >10:
        break
    else:
        print(n)


#cycle()会把传入的一个序列无限重复下去：
cs=itertools.cycle('ABC')
#for x in cs:
#    print(x)

#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns=itertools.repeat('AB',3)
for n in ns:
    print(n)

#会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
naturals=itertools.count(1)
ns=itertools.takewhile(lambda x:x<=10,naturals)
print(list(ns))

#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

#groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key,group in itertools.groupby('AAABBBCCDDDDD'):
    print(key,list(group))
















