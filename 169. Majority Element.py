# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 21:41:34 2018

@author: Wu Jingwei
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        major = max(dic, key=dic.get)
        return major
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = collections.defaultdict(int)
        for i in nums:
            dic[i] += 1
        major = max(dic, key=dic.get)
        return major