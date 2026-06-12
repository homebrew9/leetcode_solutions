from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hsh = dict()
        for p, c, left in descriptions:
            if p in hsh:
                pNode = hsh[p][0]
            else:
                pNode = TreeNode(p)
                hsh[p] = [pNode, None]
            if c in hsh:
                cNode = hsh[c][0]
                hsh[c][1] = pNode
            else:
                cNode = TreeNode(c)
                hsh[c] = [cNode, pNode]
            if left == 1:
                pNode.left = cNode
            elif left == 0:
                pNode.right = cNode
        for k, v in hsh.items():
            if v[1] is None:
                return v[0]

# Main section
# descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# descriptions = [[1,2,1],[2,3,0],[3,4,1]]


