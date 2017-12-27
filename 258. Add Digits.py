# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 23:02:34 2017

@author: Wu Jingwei
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<=9:
            return num
        while num>9:
            s=0
            while num>=1:
                s+=num%10 #s=9, n=1
                num/=10
            num =s
        return num
