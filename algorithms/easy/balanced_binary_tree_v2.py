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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, level):
            if node is None:
                return level
            left = dfs(node.left, level+1)
            right = dfs(node.right, level+1)
            if abs(left - right) > 1:
                self.is_balanced = False
            return max(left, right)
        self.is_balanced = True
        dfs(root, 0)
        return self.is_balanced

# Main section
for btree in [
                ('[3,9,20,null,null,15,7]'),
                ('[1,2,2,3,3,null,null,4,4]'),
                ('[]'),
                ('[1]'),
                ('[1,2,2,3,null,null,3,4,null,null,4]'),
             ]:
    print(f'btree = {btree}')
    root = deserialize(btree)
    sol = Solution()
    r = sol.isBalanced(root)
    print(f'r = {r}')
    print('===========================')


