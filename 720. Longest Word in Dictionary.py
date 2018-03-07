# -*- coding: utf-8 -*-
"""
Created on Tue Mar 06 23:02:11 2018

@author: Wu Jingwei
"""

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = sorted(list(set(words)))
        if not words:
            return ''
        dic={}
        for i in words:
            if len(i)==1:
                dic[i] = 1
            elif i[:-1] not in dic:
                continue
            else:
                dic[i]=len(i)
        max_len = len(max(dic, key=dic.get))
        res = [key for key in dic if len(key)==max_len]
        return min(res)
                