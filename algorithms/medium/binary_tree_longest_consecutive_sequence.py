from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(node, expected_val, length=0):
            if not node:
                return 0
            if node.val == expected_val:
                length += 1
            else:
                length = 1
            left_streak = dfs(node.left, node.val + 1, length)
            right_streak = dfs(node.right, node.val + 1, length)
            return max(length, left_streak, right_streak)
        res = dfs(root, root.val) # type: ignore
        return res

# Main section
#  [1,null,3,2,4,null,null,null,5] => 3
#  [2,null,3,2,null,1] => 2



