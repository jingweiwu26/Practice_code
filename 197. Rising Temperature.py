# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 22:06:05 2018

@author: Wu Jingwei
"""

# Write your MySQL query statement below
select w1.Id from Weather w1
join Weather w2 on to_days(w1.Date)=to_days(w2.Date)+1
where w1.Temperature > w2.Temperature;