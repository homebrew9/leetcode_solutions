#
# I am trying out the maximum depth for Binary Tree first.
# If this works, then v1 will have the code for N-ary Tree.
#
from typing import List

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

def deserialize(string):
    #print(f'\t>>> string = {string}')
    if string == '{}':
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

#class BinaryTree:
#    def traverseInOrderHelper(self, node, res):
#        if node:
#            if node.left:
#                self.traverseInOrderHelper(node.left, res)
#            res.append(node.val)
#            if node.right:
#                self.traverseInOrderHelper(node.right, res)
#
#    def traverseInOrder(self, root):
#        # :type root: TreeNode
#        # :rtype List[int]
#        res = []
#        self.traverseInOrderHelper(root, res)
#        return res

#class BinaryTree:
#    def traverseTree(self, root):
#        def dfs(node, res):
#            if node:
#                if node.left:
#                    dfs(node.left, res)
#                res.append(node.val)
#                if node.right:
#                    dfs(node.right, res)
#        res = []
#        dfs(root, res)
#        return res

class BinaryTree:
    def traverseTree(self, root):
        def dfs(node):
            if node is None:
                return 0
            print(f'\tEntered: node = {node.val}')
            left = dfs(node.left)
            right = dfs(node.right)
            print(f'\t\tnode = {node.val} ; left, right = {left}, {right}')
            return 1 + max(left, right)

        depth = dfs(root)
        return depth

# Main section
for btree in [
                '[1,2,3,4,5,null,null,null,6]',
                '[1,2,3,null,4,null,5,6,null,null,7,8,null]',
                '[1,2,3,null,4,null,5,6,null,null,7,null,null,8,null]',
             ]:
    print(f'btree = {btree}')
    root = deserialize(btree)
    bt = BinaryTree()
    r = bt.traverseTree(root)
    print(f'r = {r}')
    print('=======================')

