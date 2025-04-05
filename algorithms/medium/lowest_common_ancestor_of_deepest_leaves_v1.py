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
        def dfs(node):
            if not node:
                return (None, 0)
            left_node, left_height = dfs(node.left)
            right_node, right_height = dfs(node.right)
            # If heights are same, current node is LCA. Otherwise
            # return the root of longer subtree.
            if left_height == right_height:
                return (node, left_height + 1)
            if left_height > right_height:
                return (left_node, left_height + 1)
            if right_height > left_height:
                return (right_node, right_height + 1)
        lca, _ = dfs(root)
        return lca

# Test cases
#[3,5,1,6,2,0,8,null,null,7,4]
#[1]
#[0,1,3,null,2]

