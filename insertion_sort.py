# -*- coding: utf-8 -*-
"""
Created on Sat Dec 09 20:51:53 2017

@author: Wu Jingwei
"""

# insertion_sort

def insertion_sort(a_list):
    for position in range(1, len(a_list)):
        current_value = a_list[position]
        while position-1>=0 and a_list[position-1]>current_value:
            a_list[position] = a_list[position-1]
            position-=1
        a_list[position]= current_value
    return a_list

l=[54,26,92,17,77,31,44,55,20]
print insertion_sort(l)