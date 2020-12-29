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

    class Solution:
        def maxArea(self, height: List[int]) -> int:
            combinations = [(height_i, height_j, abs(idx_i-idx_j)) 
                            for idx_i, height_i in enumerate(height) 
                            for idx_j, height_j in enumerate(height)]
            max_area = max(combinations, key=lambda x: min(x[0], x[1]) * x[2])
            return min(max_area[0], max_area[1]) * max_area[2]
    
    class Solution:
        def maxArea(self, height: List[int]) -> int:
            idx_l = 0
            idx_r = len(height) - 1
            max_area = 0
            while idx_l != idx_r:
                max_area = max(max_area, min(height[idx_l], height[idx_r]) 
                               * abs(idx_l - idx_r))
                if height[idx_l] <= height[idx_r]:
                    idx_l += 1
                else:
                    idx_r -= 1 
            return max_area
        
