import math
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftdepth = self.getdepth(root)
        rightdepth = self.getdepth(root)

        if leftdepth == rightdepth:
            return int(math.pow(2, leftdepth)) + self.countNodes(root.right) 
        else:
            return int(math.pow(2, rightdepth)) + self.countNodes(root.left)

    def getdepth(self, root):
        if not root:
            return 0
        return 1 + self.getdepth(root.left)

# Main section
for arr_btree in [
                    '[1,2,3,4,5,6]',
                    '[]',
                    '[1]',
                 ]:
    print(f'arr_btree = {arr_btree}')
    root = deserialize(arr_btree)
    sol = Solution()
    r = sol.countNodes(root)
    print(f'r = {r}')
    print('===========================')

