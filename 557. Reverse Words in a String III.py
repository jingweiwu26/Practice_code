# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 22:39:51 2018

@author: Wu Jingwei
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([word[::-1] for word in s.split(' ')]) 