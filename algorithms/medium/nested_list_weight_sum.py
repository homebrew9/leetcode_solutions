from typing import List
from collections import deque

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # We use BFS here. If we encounter a list at a particular
        # level, then we append it to the dq so that it could be
        # processed at the next level iteration.
        dq = deque(nestedList)
        depth = 1
        res = 0
        while dq:
            size = len(dq)
            level_sum = 0
            for _ in range(size):
                curr = dq.popleft()
                if curr.isInteger():
                    level_sum += curr.getInteger() # type: ignore
                else:
                    dq.extend(curr.getList()) # type: ignore
            res += level_sum * depth
            depth += 1
        return res

# Main section
#  nestedList = [[1,1],2,[1,1]]
#  nestedList = [1,[4,[6]]]
#  nestedList = [0]






