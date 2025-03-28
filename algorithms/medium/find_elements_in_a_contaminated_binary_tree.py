# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def dfs(node, val):
            if node:
                dfs(node.left, 2*val + 1)
                node.val = val
                self.vals.add(val)
                dfs(node.right, 2*val + 2)
        self.vals = set()
        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.vals


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
