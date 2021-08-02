# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 09:31:28 2017

@author: Wu Jingwei
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n==1:
            return x
        if n==-1:
            return 1/x
        if n%2==0:
            return self.myPow(x, n/2)**2
        if n%2==1:
            return self.myPow(x,n-1)*x

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 1
        if n < 0 :
            x = 1/x
            n *= -1
        if n == 1:
            return x
        if n == 0:
            return 1
        while n > 1:
            if n % 2 == 0:
                return self.myPow(x, n/2) ** 2
            if n % 2 == 1:
                return self.myPow(x, n-1) * x
            
 class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            x = 1/x
            n *= -1
            return self.myPow(x, n)
        #   return 1 / self.myPow(x, -n) -- causes over flow
        elif n % 2 == 0:
            return self.myPow(x, n / 2)**2
        elif n % 2 == 1:
            return x * self.myPow(x, n - 1)
