# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 17:43:41 2018

@author: Wu Jingwei
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # m == 3, n == 7
        if m == 1 or n == 1:
            return 1
        res=[[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            res[i][0] = 1
        for i in range(m):
            res[0][i] = 1
        for i in range(1,n):
            for j in range(1,m):
                res[i][j]=res[i-1][j] + res[i][j-1]
                print res[i-1][j], res[i][j-1], res[i][j]
        return res[i][j]