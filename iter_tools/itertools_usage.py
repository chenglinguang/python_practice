#!/usr/bin/env python3

#-*-coding:utf-8-*-

import itertools 

naturals=itertools.count(1)

for n in naturals:
    if n <=5:
        print(n) 
    else:
        break


cs=itertools.cycle('ABC')
#for x in cs:
#    print(x)

ns=itertools.repeat('A',3)
for w in ns:
    print(w)



naturals=itertools.count(1)

ns=itertools.takewhile(lambda x:x<=10,naturals)
print(list(ns))



for c in itertools.chain('ABC','XYZ'):
    print(c)


for key,group in itertools.groupby('AAABBCCCC'):
    print(key,list(group))









