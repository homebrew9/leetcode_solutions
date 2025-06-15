from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        def dfs_total_value(node):
            if not node:
                return 0
            left_val = dfs_total_value(node.left)
            right_val = dfs_total_value(node.right)
            return left_val + node.val + right_val
        def dfs_check(node):
            left_val = dfs_check(node.left) if node.left else 0
            right_val = dfs_check(node.right) if node.right else 0
            if left_val + node.val + right_val == target and node != root:
                self.can_be_partitioned = True
            return left_val + node.val + right_val
        total_value = dfs_total_value(root)
        #print(total_value)
        if total_value % 2 == 1:
            return False
        target = total_value // 2
        self.can_be_partitioned = False
        dfs_check(root)
        return self.can_be_partitioned

# Main section
#[5,10,10,null,null,2,3]
#[1,2,10,null,null,2,20]


