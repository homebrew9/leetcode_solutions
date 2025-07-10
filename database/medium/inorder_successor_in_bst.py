from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def dfs(node):
            if node:
                dfs(node.left)
                self.res.append(node)
                if node == p:
                    self.ind = len(self.res) - 1
                dfs(node.right)
        self.ind = None
        self.res = list()
        dfs(root)
        return None if self.ind + 1 >= len(self.res) else self.res[self.ind + 1]

# Main section
# [2,1,3], 1
# [5,3,6,2,4,null,null,1], 6


















