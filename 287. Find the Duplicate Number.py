# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 16:03:04 2018

@author: Wu Jingwei
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        while l <= r:
            m = (l+r)/2
            count = sum(1 for n in nums if n <= m)
            if count <= m:
                l=m+1
            else:
                r=m-1
        return l