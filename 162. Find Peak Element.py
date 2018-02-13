# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 23:38:31 2018

@author: Wu Jingwei
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size=len(nums)
        for i in range(1, size-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
        if size==1 or nums[0]>nums[1]:
            return 0
        return size-1

class Solution(object):
    def findPeakElement(self, nums):
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)/2
            if nums[mid]<nums[mid+1]:
                left=mid+1
            else:
                right=mid
        return left