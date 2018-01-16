# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 23:40:49 2018

@author: Wu Jingwei
"""

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        size=len(A)
        count=0
        from itertools import product
        p = product(xrange(size), repeat=4)
        for idx_a, idx_b, idx_c, idx_d in p:
            if A[idx_a] + B[idx_b] + C[idx_c] + D[idx_d] == 0:
                count+=1
        return count

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        size=len(A)
        count=0
        from itertools import product
        dic = collections.defaultdict(int)
        p_ab = product(xrange(size), repeat=2)
        for idx_a, idx_b in p_ab:
            dic[A[idx_a] + B[idx_b]] += 1
        p_cd = product(xrange(size), repeat=2)
        for idx_c, idx_d in p_cd:
            count+=dic[-(C[idx_c]+D[idx_d])]
        return count
        