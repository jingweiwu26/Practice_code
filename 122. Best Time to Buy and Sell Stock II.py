# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 21:26:16 2017

@author: Wu Jingwei
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p=0
        size=len(prices)
        for i in range(size-1):
            if prices[i+1]>prices[i]:
                p+= (prices[i+1]-prices[i])
        return p

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp0 = 0 # state when not holding
        dp1 = -prices[0] # state when holding
        for p in prices[1:]:
            dp0 = max(dp0, dp1 + p)
            dp1 = max(dp1, dp0 - p)
            
        return dp0
