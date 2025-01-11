#
# Possibly the best explanation of this algorithm, by user "zayne_siew"
# Ref: https://leetcode.com/problems/diameter-of-binary-tree/discuss/1515564/Python-Easy-to-understand-solution-w-Explanation
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
        # stores the maximum diameter calculated
        self.diameter = 0

    def depth(self, node: Optional[TreeNode]) -> int:
        # This function needs to do the following:
        # 1. Calculate the maximum depth of the left and right sides of the given node.
        # 2. Determine the diameter at the given node and check if its the maximum.

        # Calculate the maximum depth
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0
        print(f'\tnode.val = {node.val} ; left = {left} ; right = {right}')

        # Calculate the diameter
        self.diameter = max(self.diameter, left + right)

        # Make sure the parent node(s) get the correct depth from this node
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # root is guaranteed to be a TreeNode object
        self.depth(root)
        return self.diameter

# Main section
for btree in [
                ('[1,2,3,4,5]'),
                ('[1,2]'),
                ('[1,2,6,3,null,null,7,4,null,null,8,5,null,9,null,10,null,11,null]'),
                ('[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]'),
                ('[1,2,3,null,null,4,5,6,7,8,null,null,null,9,null,null,10]'),
             ]:
    print(f'btree = {btree}')
    root = deserialize(btree)
    sol = Solution()
    r = sol.diameterOfBinaryTree(root)
    print(f'r = {r}')
    print('===========================')


