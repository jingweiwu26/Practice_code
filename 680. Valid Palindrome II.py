# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 12:09:21 2017

@author: Wu Jingwei
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        is_pal=lambda s:s==s[::-1]
        skip_one=lambda s,x:s[:x]+s[x+1:]
        if is_pal(s):
            return True
        l=0
        r=len(s)-1
        while s[l] and s[r]:
            if s[l]!=s[r]:
                return is_pal(skip_one(s,l)) or is_pal(skip_one(s,r))
            l+=1
            r-=1
