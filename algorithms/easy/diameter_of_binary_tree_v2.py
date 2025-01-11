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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            print(f'\t\tnode.val = {node.val}')
            print(f'\t\tleft     = {left}')
            print(f'\t\tright    = {right}')
            print(f'\t\tdepth    = {1 + max(left,right)}')
            print('========')
            return 1 + max(left, right)

        r = dfs(root)
        return r

# Main section
for btree in [
                #('[1,2,3,4,5]'),
                ('[1,2,3,4,5,6,7,null,8,null,null,null,null,9,null,null,null,10,null,null,11]'),
                #('[1,2]'),
                #('[1,2,6,3,null,null,7,4,null,null,8,5,null,9,null,10,null,11,null]'),
                #('[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]'),
                #('[1,2,3,null,null,4,5,6,7,8,null,null,null,9,null,null,10]'),
             ]:
    print(f'btree = {btree}')
    root = deserialize(btree)
    sol = Solution()
    r = sol.diameterOfBinaryTree(root)
    print(f'r = {r}')
    print('===========================')

