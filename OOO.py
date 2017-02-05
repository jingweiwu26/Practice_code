# -*- coding: utf-8 -*-
"""
Created on Thu Feb 02 15:28:07 2017

@author: Wu Jingwei
"""

class Student(object):
    pass

s=Student()
s.name="Miachael"
print s.name

def set_age(self,age):
    self.age=age

from types import MethodType
s.set_age=MethodType(set_age,s)
s.set_age(25)
print s.age

