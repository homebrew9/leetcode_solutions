# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def dfs(node, depth):
            if self.i >= N:
                return
            j = self.i
            next_depth = 0
            while j < N and traversal[j] == '-':
                next_depth += 1
                j += 1
            if next_depth == depth + 1:
                next_val = ''
                while j < N and traversal[j].isdigit():
                    next_val += traversal[j]
                    j += 1
                next_node = TreeNode(int(next_val))
                if node.left is None:
                    node.left = next_node
                else:
                    node.right = next_node
                self.i = j
                dfs(next_node, next_depth)
            j = self.i
            next_depth = 0
            while j < N and traversal[j] == '-':
                next_depth += 1
                j += 1
            if next_depth == depth + 1:
                next_val = ''
                while j < N and traversal[j].isdigit():
                    next_val += traversal[j]
                    j += 1
                next_node = TreeNode(int(next_val))
                if node.left is None:
                    node.left = next_node
                else:
                    node.right = next_node
                self.i = j
                dfs(next_node, next_depth)
        N = len(traversal)
        head_val = ''
        i = 0
        while i < N and traversal[i].isdigit():
            head_val += traversal[i]
            i += 1
        head_node = TreeNode(int(head_val))
        self.i = i
        dfs(head_node, 0)
        return head_node

# Main section
# "1-2--3--4-5--6--7"
# "1-2--3---4-5--6---7"
# "1-401--349---90--88"
