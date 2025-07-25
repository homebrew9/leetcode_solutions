from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return list()
        dq = deque()
        depth = 0
        dq.append(root)
        res = list()
        while dq:
            if depth % 2 == 0:
                res.append([node.val for node in dq])
            else:
                res.append(list(reversed([node.val for node in dq])))
            size = len(dq)
            for _ in range(size):
                curr = dq.popleft()
                if curr.left is not None:
                    dq.append(curr.left)
                if curr.right is not None:
                    dq.append(curr.right)
            depth += 1
        return res

# Main section
# [3,9,20,null,null,15,7]
# [1]
# []

























