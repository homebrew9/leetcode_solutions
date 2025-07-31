from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def dfs(node):
            if node:
                dfs(node.left)
                self.values.append(node.val)
                dfs(node.right)
        self.values = list()
        dfs(root)
        res = list()
        min_val = float('inf')
        for i in range(k-1, len(self.values)):
            tmp = 0
            for j in range(i - k + 1, i + 1):
                tmp += abs(self.values[j] - target)
            if tmp < min_val:
                min_val = tmp
                res = self.values[i-k+1:i+1][:]
        return res

# Main section
# [4,2,5,1,3], 3.714286, 2
# [1], 0.000000, 1

























