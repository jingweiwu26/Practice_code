# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:17:58 2018

@author: Wu Jingwei
"""

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {i**2:1 for i in range(1,n+1) if i**2 <= n}
        dp[0] = 0
        for i in range(1,n+1):
            if i not in dp:
                dp[i] = dp[i-1]+1
            
        for i in range(1, n+1):
            y=1
            while i+y*y<=n:
                if dp[i+y*y]>dp[i]+1:
                    dp[i+y*y] = dp[i]+1
                y+=1
        return dp[n]