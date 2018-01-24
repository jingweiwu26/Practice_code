# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 22:30:38 2018

@author: Wu Jingwei
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums.count(0)>1:
            return [0] * len(nums)

        product = 1
        for i in nums:
            if i==0:
                continue
            product*=i
        
        if nums.count(0)==0:
            return [product/i for i in nums]
        
        else:
            return [0 if i!=0 else product for i in nums]

        
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[0] * len(nums)
        temp=1
        for i in xrange(len(nums)):
            res[i]=temp
            temp*=nums[i]
        
        temp=1
        for i in xrange(len(nums)-1,-1,-1):
            res[i]*=temp
            temp*=nums[i]
        
        return res
