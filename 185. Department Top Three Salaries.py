# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:48:31 2018

@author: Wu Jingwei
"""

with t as (
select d.Name as Department, 
       e.Name as Employee, 
       e.Salary,
       row_number() over(partition by Department order by Salary desc) as RN
from   Employee e 
join   Department d on e.DepartmentId = d.Id)
select Department, 
       Employee,
       Salary from t
where  t.RN <=3;