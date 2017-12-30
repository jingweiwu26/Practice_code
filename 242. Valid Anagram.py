# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 10:11:43 2017

@author: Wu Jingwei
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic_s = self.dic_count(s)
        dic_t = self.dic_count(t)
        if dic_s != dic_t:
            return False
        return True
    def dic_count(self, string):
        dic={}
        for i in string:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        return dic