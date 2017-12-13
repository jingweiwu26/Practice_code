# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 12:07:51 2017

@author: Wu Jingwei
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        current_stg = [0,1,1,0]
        for i in range(rowIndex-1):
            temp = [current_stg[j]+current_stg[j+1] for j in range(len(current_stg)-1)]
            current_stg = [0] + temp +[0]
        return temp