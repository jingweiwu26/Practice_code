# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 22:39:52 2018

@author: Wu Jingwei
"""

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        l = list(moves)
        if l.count('U') == l.count('D') and l.count('L') == l.count('R'):
            return True
        return False