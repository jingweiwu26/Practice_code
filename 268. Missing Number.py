# -*- coding: utf-8 -*-
"""
Created on Mon Feb 05 22:00:34 2018

@author: Wu Jingwei
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size=len(nums)+1
        l=set(range(size))
        for i in nums:
            l.remove(i)
        return list(l)[0]

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = reduce(operator.xor, nums)
        b = reduce(operator.xor, range(len(nums) + 1))
        return a ^ b