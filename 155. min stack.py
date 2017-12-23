# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 10:03:08 2017

@author: Wu Jingwei
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.stack_min=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.stack_min or x<=self.stack_min[-1]:
            self.stack_min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack.pop()==self.stack_min[-1]:
            self.stack_min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack_min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()