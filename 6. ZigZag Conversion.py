# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 22:05:03 2018

@author: Wu Jingwei
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        g=self.gen(numRows)
        res=[[] for i in range(numRows)]
        row_to_append=0
        for i in s:
            res[row_to_append].append(i)
            row_to_append+=g.next()
        return "".join(reduce(lambda x,y: x+y, res))
            
    
    def gen(self, numRows):
        round=numRows-1
        sign=0
        res=-1
        while True:
            if sign == round or sign == 0:
                res *= -1
            sign += res
            yield res