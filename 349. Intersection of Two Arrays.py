# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 23:26:00 2018

@author: Wu Jingwei
"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1)&set(nums2))