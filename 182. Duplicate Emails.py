# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 22:07:37 2018

@author: Wu Jingwei
"""

select Email from (select Email, count(1) cnt from Person group by Email having cnt >1) c;