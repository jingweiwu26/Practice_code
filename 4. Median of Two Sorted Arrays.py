# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 21:58:12 2018

@author: Wu Jingwei
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size_1=len(nums1)
        size_2=len(nums2)
        idx_1=0
        idx_2=0
        merged_list = []
        while idx_1<size_1 and idx_2<size_2:
            if nums1[idx_1] < nums2[idx_2]:
                merged_list.append(nums1[idx_1])
                idx_1+=1
            else:
                merged_list.append(nums2[idx_2])
                idx_2+=1
        if idx_1==size_1:
            merged_list += nums2[idx_2:]
        if idx_2==size_2:
            merged_list += nums1[idx_1:]
        while len(merged_list)>2:
            merged_list.pop()
            merged_list.pop(0)
        if len(merged_list) == 1:
            return merged_list[0]
        else:
            return sum(merged_list)/2.0