# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 18:26:54 2018

@author: Wu Jingwei
"""

# Write your MySQL query statement below
delete from Person where Id not in (select t.Id from 
(select min(Id) Id from Person pp group by pp.Email) t); 
