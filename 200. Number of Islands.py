# -*- coding: utf-8 -*-
"""
Created on Tue Jan 02 23:28:12 2018

@author: Wu Jingwei
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count=0
        n_rows=len(grid)
        n_cols=len(grid[0])
        for i in xrange(n_rows):
            for j in xrange(n_cols):
                if grid[i][j]=='1':
                    count+=1
                    self.sink(grid, i, j, n_rows, n_cols)
        return count
    def sink(self, grid, i, j, n_rows, n_cols):
        grid[i][j]='0'
        if i+1<n_rows and grid[i+1][j] =='1':
            self.sink(grid,i+1,j, n_rows, n_cols)
        if i-1>=0 and grid[i-1][j] =='1':
            self.sink(grid,i-1,j, n_rows, n_cols)
        if j+1<n_cols and grid[i][j+1] =='1':
            self.sink(grid,i,j+1, n_rows, n_cols)
        if j-1>=0 and grid[i][j-1] =='1':
            self.sink(grid,i,j-1, n_rows, n_cols)
        