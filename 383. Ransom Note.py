# -*- coding: utf-8 -*-
"""
Created on Thu Feb 08 23:50:51 2018

@author: Wu Jingwei
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic_a={}
        dic_b={}
        for i in ransomNote:
            if i not in dic_a:
                dic_a[i]=0
            dic_a[i]+=1
        for i in magazine:
            if i not in dic_b:
                dic_b[i]=0
            dic_b[i]+=1
        for i in dic_a:
            if dic_b.get(i,0)<dic_a[i]:
                return False
        return True