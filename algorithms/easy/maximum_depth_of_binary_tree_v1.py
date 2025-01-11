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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        def dfs(node, depth):
            if node:
                if depth > self.max_depth:
                    self.max_depth = depth
                dfs(node.left, depth+1)
                dfs(node.right, depth+1)
        depth = 1
        dfs(root, depth)
        return self.max_depth

# Main section
for btree in [
                ('3,9,20,null,null,15,7]'),
                ('[1,null,2]'),
                ('[]'),
                ('[1]'),
             ]:
    print(f'btree = {btree}')
    root = deserialize(btree)
    sol = Solution()
    r = sol.maxDepth(root)
    print(f'r = {r}')
    print('===========================')

