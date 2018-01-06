class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        m=0
        n=0
        res=[]
        while m<len(nums1) and n<len(nums2):
            if nums1[m]==nums2[n]:
                res.append(nums1[m])
                m+=1
                n+=1
            elif nums1[m] > nums2[n]:
                n+=1
            elif nums1[m] < nums2[n]:
                m+=1
        return res

@author: Wu Jingwei
"""

