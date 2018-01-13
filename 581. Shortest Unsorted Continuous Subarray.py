# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 12:41:05 2018

@author: Wu Jingwei
"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums==sorted(nums):
            return 0
        
        size=len(nums)
        for i in range(size):
            if nums[i] != min(nums[i:]):
                start_idx=i
                break
        for i in reversed(range(size)):
            if nums[:i] and nums[i] != max(nums[:i+1]):
                end_idx=i
                break
        try:
            return end_idx-start_idx+1
        except:
            return 0