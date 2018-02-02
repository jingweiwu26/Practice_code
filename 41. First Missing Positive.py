# -*- coding: utf-8 -*-
"""
Created on Thu Feb 01 22:40:42 2018

@author: Wu Jingwei
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        nums=sorted(list(set(nums)))
        nums=filter(lambda x:x>0, nums)
        
        if not nums:
            return 1
        
        if nums[0]>1:
            return 1
        
        size=len(nums)
        print nums
        for i in range(size):
            if nums[i]!=i+1:
                return i+1
        return i+2