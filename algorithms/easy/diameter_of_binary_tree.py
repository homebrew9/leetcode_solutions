#
# Doesn't work!
#
from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

def deserialize(string):
    #print(f'\t>>> string = {string}')
    if string == '{}' or string == '[]':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    #print(f'\t>>> nodes = {nodes}')
    kids = nodes[::-1]
    #print(f'\t>>> kids = {kids}')
    root = kids.pop()
    #print(f'\t>>> root = {root}')
    for node in nodes:
        #print(f'\t\t>>> node = {node}')
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

class Solution:
    def __init__(self):
        self.left_depth = 0
        self.right_depth = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, side, d):
            if node:
                print(f'\tnode.val = {node.val} ; depth = {d}')
                if node.left is None and node.right is None:
                    if side == 'left':
                        self.left_depth = max(self.left_depth, d)
                    elif side == 'right':
                        self.right_depth = max(self.right_depth, d)
                dfs(node.left, side, d+1)
                dfs(node.right, side, d+1)

        dfs(root.left, 'left', 1)
        dfs(root.right, 'right', 1)
        return self.left_depth + self.right_depth

# Main section
for btree in [
                #('[1,2,3,4,5]'),
                #('[1,2]'),
                #('[1,2,6,3,null,null,7,4,null,null,8,5,null,9,null,10,null,11,null]'),
                ('[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]'),
             ]:
    print(f'btree = {btree}')
    root = deserialize(btree)
    sol = Solution()
    r = sol.diameterOfBinaryTree(root)
    print(f'r = {r}')
    print('===========================')

