# -*- coding: utf-8 -*-
"""
Created on Sat Jan 06 12:09:32 2018

@author: Wu Jingwei
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size=len(nums)
        for i in range(size-1):
            if nums[i+1]<nums[i]:
                return nums[i+1]
        return nums[0]