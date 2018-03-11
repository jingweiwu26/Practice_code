# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:34:30 2018

@author: Wu Jingwei
"""

# Write your MySQL query statement below
                     
update salary set sex = (case when sex = 'm' then 'f'
                              when sex = 'f' then 'm' end);