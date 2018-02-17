# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 13:40:14 2018

@author: Wu Jingwei
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size=len(height)
        left=0
        right=size-1
        max_area=0
        while left < right:
            if height[left] < height[right]:
                area = (right-left) * height[left]
                if area > max_area:
                    max_area = area
                left += 1
            else:
                area = (right-left) * height[right]
                if area > max_area:
                    max_area = area
                right -= 1
        return max_area