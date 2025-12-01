from typing import List
from collections import deque

#"""
#This is the interface that allows for creating nested lists.
#You should not implement it, or speculate about its implementation
#"""
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int: # type: ignore
        queue = deque(nestedList)
        unweighted_sum = 0
        weighted_sum = 0
        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                item = queue.popleft()
                if item.isInteger():
                    level_sum += item.getInteger() # type: ignore
                else:
                    queue.extend(item.getList()) # type: ignore
            unweighted_sum += level_sum
            weighted_sum += unweighted_sum  # Accumulates inverse weights!
        return weighted_sum

# Main section
#  nestedList = [[1,1],2,[1,1]]
#  nestedList = [1,[4,[6]]]








