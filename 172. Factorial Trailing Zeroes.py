# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:31:59 2018

@author: Wu Jingwei
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)