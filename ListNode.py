#!/usr/bin/env python3 

#-*- coding:utf-8 -*-

__author__='Cheng Linguang'

#listNode simple definition 

class ListNode(object):

    def __init__(self,val):
        self._data=val
        self._next=None
    
    @property 
    def val(self):
        return self._data
    
    @property
    def next(self):
        return self._next

    @val.setter
    def val(self,val):
        self._data=val

    @next.setter
    def next(self,val)
        self.next=val
        
