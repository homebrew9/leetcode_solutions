"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        def dfs(node):
            if node == leaf:
                self.res = node
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        def change_root(parent_node, child_node):
            if child_node == root:
                child_node.parent = parent_node
                return
            if child_node.left:
                child_node.right = child_node.left
                child_node.left = None
            pnode = child_node.parent
            if pnode:
                if pnode.left == child_node:
                    pnode.left = None
                if pnode.right == child_node:
                    pnode.right = None
                child_node.left = pnode
            child_node.parent = parent_node
            change_root(child_node, child_node.left)
        self.res = None
        dfs(root)
        change_root(None, self.res)
        return self.res
        

