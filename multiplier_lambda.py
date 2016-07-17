#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

def multiplier():
    return [lambda x : i*x for i in range(4)]

print([m(2) for m in multiplier()])

#solution:

def multiplier_re():
    return [lambda x ,i=i:i*x for i in range(4)]



