# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 23:08:03 2018

@author: Wu Jingwei
"""

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def sort_key(ppl):
            return -ppl[0], ppl[1]
        people = sorted(people, key=sort_key)
        for idx, ppl in enumerate(people):
            if idx == people[idx][1]:
                continue
            temp = ppl
            target_position = ppl[1]
            people.pop(idx)
            people.insert(target_position, temp)
        return people