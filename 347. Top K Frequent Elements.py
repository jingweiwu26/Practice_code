# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 23:02:24 2018

@author: Wu Jingwei
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=0
            dic[i]+=1
        res=[]
        for i in range(k):
            top = max(dic, key=dic.get)
            res.append(top)
            del dic[top]
        return res