# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 15:30:14 2018

@author: Wu Jingwei
"""

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        max_length = 0
        dic={-1:0}
        for line in input.splitlines():
            depth = line.count('\t')
            line=line.lstrip('\t')
            if '.' in line:
                max_length = max(max_length, dic[depth-1]+len(line))
            else:
                dic[depth]=len(line)+1+dic[depth-1]
        print dic
        return max_length