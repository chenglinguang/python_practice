#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

class Parent(object):
    x=1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print (Parent.x,Child1.x,Child2.x)
Child1.x=2
print (Parent.x,Child1.x,Child2.x)
Parent.x=3
print (Parent.x,Child1.x,Child2.x)


def div1(x,y):
    print("%s/%s = %s" % (x, y, x/y))

def div2(x,y):
    print("%s//%s = %s" % (x, y, x//y))

div1(5,2)
div1(5.,2)
div2(5,2)
div2(5.,2.)




