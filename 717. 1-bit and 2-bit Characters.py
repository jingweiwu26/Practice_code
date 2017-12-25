# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 11:36:31 2017

@author: Wu Jingwei
"""

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        idx=0
        size=len(bits)
        while idx < size:
            if idx == size-1:
                return True
            if bits[idx]==0:
                idx+=1
            if bits[idx]==1:
                idx+=2
        return False
            
    
    
    #dd 01010
    #ds 0110
    #sd 0010
    #ss 01000