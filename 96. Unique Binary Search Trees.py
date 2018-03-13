# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 22:02:20 2018

@author: Wu Jingwei
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp= [1, 1, 2]
        if n <= 2:
            return dp[n]
        for i in xrange(3, n+1):
            _ = 0
            j, k = xrange(0, i), xrange(i-1, -1, -1)
            for p, q in zip(j,k):
                _ += (dp[p]*dp[q])
            dp.append(_)
        return dp[n]