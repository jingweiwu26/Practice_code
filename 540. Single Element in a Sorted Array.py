# -*- coding: utf-8 -*-
"""
Created on Fri Mar 09 22:14:40 2018

@author: Wu Jingwei
"""

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x,y: x^y, nums)