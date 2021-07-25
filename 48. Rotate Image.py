# -*- coding: utf-8 -*-
"""
Created on Thu Mar 01 22:22:35 2018

@author: Wu Jingwei
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range(size):
            for j in range(i+1,size):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in matrix:
            i.reverse()
 
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        step_1 = [list(i)for i in zip(*matrix)]
        print(step_1)
        step_m = [i[::-1] for i in step_1]
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                matrix[row][col] = step_m[row][col]
        return matrix
    
        # 1 2 3
        # 4 5 6
        # 7 8 9
        
        # 1 4 7
        # 2 5 8
        # 3 6 9 
