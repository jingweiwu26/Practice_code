# -*- coding: utf-8 -*-
"""
Created on Fri Feb 03 21:17:43 2017

@author: Wu Jingwei
"""

class Student(object):
    
    __slots__= ('name','age','set_age')
    
    def __init__(self,name):
        self.name=name

k=Student("Andrew")

print k.name

from types import MethodType

def set_age(self,age):
    self.age=age
    
k.set_age=MethodType(set_age,k)

k.set_age(25)

print k.age