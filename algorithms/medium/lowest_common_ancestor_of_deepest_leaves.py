from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Intuition: Having two return values (LCA, height_from_leaf_to_root) simplifies a
        # lot of the implementation details.
        # TC, SC = O(N), O(h) where h = height of tree, which can be N in case of degenerate tree.
        # It traverses the tree only once, unlike earlier approaches that traversed
        # twice - once to find deepest leaves and then again to find lca.
        # NeetcodeIO channel
        def dfs(node, depth):
            if not node:
                return (None, depth + 1)
            left_node, left_depth = dfs(node.left, depth + 1)
            right_node, right_depth = dfs(node.right, depth + 1)
            # If depths are same, current node is LCA. Otherwise
            # return the root of longer subtree.
            if left_depth > right_depth:
                return (left_node, left_depth)
            elif right_depth > left_depth:
                return (right_node, right_depth)
            return (node, left_depth)
        lca, _ = dfs(root, 0)
        return lca

# Test cases
#[3,5,1,6,2,0,8,null,null,7,4]
#[1]
#[0,1,3,null,2]

