# -*- coding: utf-8 -*-
"""
Created on Sat Mar 03 23:04:42 2018

@author: Wu Jingwei
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    print k, s[k:i]
                    dp[i] = True
        return dp[-1]