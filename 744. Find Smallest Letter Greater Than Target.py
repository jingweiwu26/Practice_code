# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 23:21:18 2018

@author: Wu Jingwei
"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        size=len(letters)
        l=0
        r=size-1
        
        while l<=r:
            m=(l+r)/2
            print l,m,r
            if letters[m]<=target:
                l=m+1
            else:
                if m==0:
                    return letters[0]
                if letters[m-1]<=target:
                    return letters[m]
                r=m-1
        return letters[0]
        