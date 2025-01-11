from typing import List

#class BinaryTree:
#    def traverseTree(self, root):
#        def dfs(node):
#            if node is None:
#                return 0
#            print(f'\tEntered: node = {node.val}')
#            left = dfs(node.left)
#            right = dfs(node.right)
#            print(f'\t\tnode = {node.val} ; left, right = {left}, {right}')
#            return 1 + max(left, right)
#
#        depth = dfs(root)
#        return depth

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node):
            if node is None:
                return 0
            depths = []
            for child in node.children:
                depths += [dfs(child)]
            return 1 + (max(depths) if depths else 0)

        depth = dfs(root)
        return depth

# # Main section
# for btree in [
#                 '[1,2,3,4,5,null,null,null,6]',
#                 '[1,2,3,null,4,null,5,6,null,null,7,8,null]',
#                 '[1,2,3,null,4,null,5,6,null,null,7,null,null,8,null]',
#              ]:
#     print(f'btree = {btree}')
#     root = deserialize(btree)
#     bt = BinaryTree()
#     r = bt.traverseTree(root)
#     print(f'r = {r}')
#     print('=======================')

