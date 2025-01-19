# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return False
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            if left_val and right_val:
                self.lca = node
            elif node in (p, q):
                if left_val or right_val:
                    self.lca = node
                return True
            return left_val or right_val
        self.lca = None
        dfs(root)
        return self.lca

'''
[3,5,1,6,2,0,8,null,null,7,4]
5
1
[3,5,1,6,2,0,8,null,null,7,4]
5
4
[3,5,1,6,2,0,8,null,null,7,4]
5
10
[3,5,1,6,2,0,8,null,null,7,4]
50
10
[3,5,1,6,2,0,8,null,null,7,4]
7
8
[3,5,1,6,2,0,8,null,null,7,4]
0
1
'''

