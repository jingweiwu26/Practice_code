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
