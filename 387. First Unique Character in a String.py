# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 23:59:27 2018

@author: Wu Jingwei
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import OrderedDict
        dic = OrderedDict()
        for i in s:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        for i,v in dic.iteritems():
            if v==1:
                return s.index(i)
        print dic
        return -1