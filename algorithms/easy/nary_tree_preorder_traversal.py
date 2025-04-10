"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node, res):
            if node:
                res.append(node.val)
                for child in node.children:
                    if child:
                        dfs(child, res)

        res = []
        dfs(root, res)
        return res

