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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.left_leaf_sum = 0
        def dfs(node, mark):
            if node:
                if mark == 'l' and node.left is None and node.right is None:
                    self.left_leaf_sum += node.val
                dfs(node.left, 'l')
                dfs(node.right, 'r')
        dfs(root, '')
        return self.left_leaf_sum

# Main section
for btree in [
                ('[3,9,20,null,null,15,7]'),
                ('[1]'),
                ('[1,2,2,3,3,null,null,4,4]'),
                ('[1,2,2,3,null,null,3,4,null,null,4]'),
             ]:
    print(f'btree = {btree}')
    root = deserialize(btree)
    sol = Solution()
    r = sol.sumOfLeftLeaves(root)
    print(f'r = {r}')
    print('===========================')
       
