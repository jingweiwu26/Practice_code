# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:05:33 2017

@author: Wu Jingwei
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        lowest=prices[0]
        max_profit=0
        for i in prices:
            if i <lowest:
                lowest=i
                profit=0
            else:
                profit=i-lowest
            if profit>max_profit:
                max_profit=profit
        return max_profit