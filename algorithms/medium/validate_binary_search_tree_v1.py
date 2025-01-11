#
# Simpler solution for validate BST, by user: "brianchiang_tw"
# Ref: https://leetcode.com/problems/validate-binary-search-tree/discuss/974147/PythonJSGoC%2B%2B-O(n)-by-DFS-and-rule-w-Hint
# 
# Algorithm:
# 
# Step_#1:
# Set upper bound as maximum integer, and lower bound as minimum integer in run-time environment.
# 
# Step_#2:
# Start DFS traversal from root node, and check whether each level follow BST rules or not.
# Update lower bound and upper bound before going down to next level.
# 
# Step_#3:
# Once we find the violation, reject and early return False.
# Otherwise, accept and return True if all tree nodes follow BST rule.
# 
#
import sys
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Use maximal system integer to represent infinity
        INF = sys.maxsize
        def helper(node, lower, upper):
            if not node:
                # empty node or empty tree
                return True
            if lower < node.val < upper:
                # check if all tree nodes follow BST rule
                return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
            else:
                # early reject when we find violation
                return False
        # ----------------------------------
        return helper(node=root, lower=-INF, upper=INF)

# Main section
for arr_btree in [
                    '[2,1,3]',
                    '[5,1,4,null,null,3,6]',
                 ]:
    print(f'arr_btree = {arr_btree}')
    root = deserialize(arr_btree)
    sol = Solution()
    r = sol.isValidBST(root)
    print(f'r = {r}')
    print('===========================')


