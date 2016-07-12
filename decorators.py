#!/usr/bin/env python3 

#-*-encoding:utf-8-*-

import functools

def log(func):
    @functools.wraps(func):
    def wrapper(*args,**kw):
        print 'call %s()'% func.__name__
        return func(*args,**kw)
    return wrapper

#带参数的decorator

def log(text):
    def decorator(func):
        @functools.wraps(func):
        def wrapper(*args,**kw):
            print '%s %s():' % (text,func.__name)
        return wrapper
    return decorator



