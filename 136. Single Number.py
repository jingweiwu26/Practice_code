# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 21:29:57 2017

@author: Wu Jingwei
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for i in nums:
            result^=i
        return result
        