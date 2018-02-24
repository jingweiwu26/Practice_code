# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:20:20 2018

@author: Wu Jingwei
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        return heapq.nlargest(k, nums)[-1]