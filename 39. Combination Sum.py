# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 23:05:24 2018

@author: Wu Jingwei
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans, _path = [], []
        self.solve(0, target, _path, ans, candidates)
        return ans
 
    def solve(self, cur, target, _path, ans, candidates):
        if target == 0:
            ans.append(_path[:])
            return
        while cur < len(candidates):
            if candidates[cur] <= target:
                _path.append(candidates[cur])
                self.solve(cur, target - candidates[cur], _path, ans, candidates)
                _path.pop()
            cur += 1

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for i in range(target+1)]
        dp[0] = [[]]
        for c in candidates:
            for i in range(target + 1):
                if i >= c:
                    for ans in dp[i-c]:
                        dp[i].append(ans+[c])
        return dp[-1]
