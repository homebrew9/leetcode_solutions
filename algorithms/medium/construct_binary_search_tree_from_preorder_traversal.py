from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(low, high):
            nonlocal i
            if i < N:
                val = preorder[i]
                if low < val < high:
                    root = TreeNode(val)
                    i += 1
                    root.left = dfs(low, val)
                    root.right = dfs(val, high)
                    return root
        N = len(preorder)
        i = 0
        head = dfs(float('-inf'), float('inf'))
        return head

# Main section
#  [8,5,1,7,10,12]
#  [1,3]







