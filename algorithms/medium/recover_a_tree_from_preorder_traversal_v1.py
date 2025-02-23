# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = list()
        next_depth = 0
        next_val = ''
        for ch in traversal:
            if ch == '-':
                if len(next_val) > 0:
                    next_node = TreeNode(int(next_val))
                    while len(stack) > next_depth:
                        stack.pop()
                    if len(stack) > 0:
                        parent_node = stack[-1]
                        if parent_node.left is None:
                            parent_node.left = next_node
                        else:
                            parent_node.right = next_node
                    stack.append(next_node)
                    next_depth = 1
                    next_val = ''
                else:
                    next_depth += 1
            elif ch.isdigit():
                next_val += ch
        next_node = TreeNode(int(next_val))
        if len(stack) == 0:
            return next_node
        while len(stack) > next_depth:
            stack.pop()
        if len(stack) > 0:
            parent_node = stack[-1]
            if parent_node.left is None:
                parent_node.left = next_node
            else:
                parent_node.right = next_node
        return stack[0]

# Main section
# "1-2--3--4-5--6--7"
# "1-2--3---4-5--6---7"
# "1-401--349---90--88"

