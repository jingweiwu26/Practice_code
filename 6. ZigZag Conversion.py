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

            
class Solution:
    def convert(self, s: str, numRows: int) -> str:

    if numRows == 1:
        return s

    res = ['' for i in range(numRows)]
    gen = self.gen(numRows)
    next_row = 0
    for i in range(len(s)):
        res[next_row] = res[next_row] + s[i]
        next_row = next_row + next(gen)
    return "".join(res)

    def gen(self, numRows):
        while True:
            for _ in range(numRows-1):
                yield 1
            for _ in range(numRows-1):
                yield -1
