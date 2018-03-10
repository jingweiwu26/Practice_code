# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 13:54:21 2018

@author: Wu Jingwei
"""

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}
        

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for i in dict:
            if i not in self.dic:
                self.dic[i] = False

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for i in self.dic:
            if i == word:
                continue
            if len(i)!= len(word):
                continue
            for j in range(len(i)):
                if i[:j] + i[(j+1):] == word[:j] + word[(j+1):]:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)