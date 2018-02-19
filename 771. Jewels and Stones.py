# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:24:47 2018

@author: Wu Jingwei
"""

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count=0
        for i in S:
            if i in J:
                count+=1
        return count