# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 13:46:32 2018

@author: Wu Jingwei
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic={}
        for i in strs:
            if "".join(sorted(i)) not in dic:
                dic["".join(sorted(i))] = [i]
            else:
                dic["".join(sorted(i))].append(i)
        res=[]
        for key, value in dic.iteritems():
            res.append(value)
        return res
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            if "".join(sorted(i)) not in dic:
                dic["".join(sorted(i))] = []
            dic["".join(sorted(i))].append(i)
        
        res = []
        for i in dic:
            res.append(dic[i])
            
        return res
