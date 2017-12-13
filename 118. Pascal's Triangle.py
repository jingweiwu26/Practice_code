# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 22:03:42 2017

@author: Wu Jingwei
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        if numRows > 2:
            initial = [[1],[1,1]]
            for i in range(numRows-2):
                current = [0] + initial[-1] + [0]
                next = [current[i]+current[i+1] for i in range(len(current)-1)]
                initial.append(next)
        return initial