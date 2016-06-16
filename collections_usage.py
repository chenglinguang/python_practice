#!/usr/bin/env python3 

#-*- utf-8 -*-

from collections import namedtuple

Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x)
print(p.y)

print(isinstance(p,Point))
print(isinstance(p,tuple))

Circle=namedtuple('Circle',['x','y','z'])

c=Circle(1,2,3)
print(c.x)


#deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
#deque

from collections import deque

q=deque(['a','b','c'])
q.append('x')
q.appendleft('y')
value_1=q.pop()
value_2=q.pop()
print(value_1)
print(value_2)
value_3=q.popleft()
print(value_3)
print(q)
#print(q.reverse())
l1=[1,2,3]
l1.reverse()
print(l1)

#defaultdict
#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：

from collections import defaultdict
dd=defaultdict(lambda:'NA')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])


#OrderedDict
#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序.
#如果要保持Key的顺序，可以用OrderedDict：

from collections import OrderedDict
d=dict([('a',1),('b',2),('c',3)])

print(d)


od=OrderedDict([('a',1),('b',2),('c',3)])
print(od)

od1=OrderedDict()
od1['x']=1
od1['y']=2
od1['z']=3

print(list(od1.keys()))


#Counter
#Counter是一个简单的计数器，例如，统计字符出现的个数：

from collections import Counter
c=Counter()
for ch in 'programming':
    c[ch]=c[ch]+1

print(c)

cc=Counter()
#print(cc('nexttttt'))
dict=Counter('programming')

print(dict)






























