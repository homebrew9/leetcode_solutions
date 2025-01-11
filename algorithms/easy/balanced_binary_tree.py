#
# DOES NOT WORK FOR THE 5TH TEST CASE!!
# Tree looks like this:
#       1
#      / \
#     2   2
#    /     \
#   3       3
#  /         \
# 4           4
# 
# IT IS BALANCED FOR NODE(1), BUT NOT FOR ANY OTHER NODE!!
# Check the solution by DBabichev in v1.
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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_height = 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # We can find the max height of the left and right subtrees of the
        # root node. If diff in height > 1, then tree is not balanced.
        def maxTreeHeight(node, height):
            if node:
                height += 1
                self.max_height = max(self.max_height, height)
                #print(f'\theight = {height}')
                if node.left:
                    maxTreeHeight(node.left, height)
                if node.right:
                    maxTreeHeight(node.right, height)

        # Looks like a NULL Binary Tree is considered balanced??!!
        # Not sure why... if there is no tree, then there is no concept of
        # balance or imbalance.
        if root is None:
            return True
        maxTreeHeight(root.left, 0)
        print(self.max_height)
        left_height = self.max_height
        self.max_height = 0
        maxTreeHeight(root.right, 0)
        print(self.max_height)
        right_height = self.max_height
        if abs(left_height - right_height) > 1:
            return False
        else:
            return True

# Main section
for btree in [
                #('[3,9,20,null,null,15,7]'),
                #('[1,2,2,3,3,null,null,4,4]'),
                #('[]'),
                #('[1]'),
                ('[1,2,2,3,null,null,3,4,null,null,4]'),
             ]:
    print(f'btree = {btree}')
    root = deserialize(btree)
    sol = Solution()
    r = sol.isBalanced(root)
    print(f'r = {r}')
    print('===========================')

