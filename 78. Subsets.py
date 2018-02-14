# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 22:40:00 2018

@author: Wu Jingwei
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        for i in range(1,len(nums)+1):
            com=itertools.combinations(nums, i)
            for i in com:
                res.append(list(i))
        return res