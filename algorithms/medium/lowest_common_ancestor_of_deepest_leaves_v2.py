from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # This solution requires two DFS traversals - one for determining deepest leaves, and
        # the other for determining their LCA.
        def find_deepest_leaves(node, depth):
            if node:
                find_deepest_leaves(node.left, depth+1)
                find_deepest_leaves(node.right, depth+1)
                if depth == self.max_depth:
                    self.deepest_leaves.add(node)
                elif depth > self.max_depth:
                    self.max_depth = depth
                    self.deepest_leaves = set([node])
        def find_lca(node):
            if not node:
                return 0
            left_val = find_lca(node.left)
            right_val = find_lca(node.right)
            if node in self.deepest_leaves:
                total = 1
            else:
                total = left_val + right_val
            if total == len(self.deepest_leaves):
                if not self.lca:
                    self.lca = node
            return total
        self.max_depth = 0
        self.deepest_leaves = set()
        find_deepest_leaves(root, 0)
        self.lca = None
        find_lca(root)
        return self.lca

# Test cases
#[3,5,1,6,2,0,8,null,null,7,4]
#[1]
#[0,1,3,null,2]

