# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:56:58 2018

@author: Wu Jingwei
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        from itertools import combinations
        comb = combinations(range(2*n), n)
        res=[]
        for i in comb:
            some_list=[')']*2*n
            for j in i:
                some_list[j]='('
            res.append("".join(some_list))
        return [i for i in res if self.valid_parentheses(i)]
    
    def valid_parentheses(self, string):
        some_list=[]
        for i in string:
            if i == '(':
                some_list.append(i)
            else:
                try:
                    some_list.pop()
                except:
                    return False
        return True