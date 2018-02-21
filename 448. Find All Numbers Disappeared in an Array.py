# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 22:44:43 2018

@author: Wu Jingwei
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return list(set(range(1, len(nums)+1)) - set(nums))