"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node, res):
            if node:
                for child in node.children:
                    if child:
                        dfs(child, res)
                res.append(node.val)
        
        res = []
        dfs(root, res)
        return res

