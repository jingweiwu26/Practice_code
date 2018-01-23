# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:29:44 2018

@author: Wu Jingwei
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        
        size=len(nums)
        dic={}
        res=set()

        for i in xrange(size):
            for j in xrange(i+1,size):
                if (nums[i] + nums[j]) not in dic:
                    dic[nums[i]+nums[j]]=[[nums[i],nums[j]]]
                else:
                    dic[nums[i]+nums[j]].append([nums[i],nums[j]])
        
        for i in xrange(size):
            if -nums[i] in dic:
                for j in dic[-nums[i]]:
                    if nums[i] not in j:
                        l=[nums[i]]+j
                        t=tuple(l)
                        print res
                        res.add(t)
       
        return list(res)

    
class Solution(object):
    def threeSum(self, nums):
        if set(nums) == {0} and len(nums)>2:
            return [[0,0,0]]
        res=set()
        nums.sort()
        size=len(nums)
        for i in xrange(size-1):
            j=i+1
            k=size-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    if (nums[i], nums[j], nums[k]) not in res:
                        res.add((nums[i], nums[j], nums[k]))
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
        return list(res)