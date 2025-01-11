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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float('-inf')
        # Postorder traversal of subtree rooted at "node"
        def gain_from_subtree(node):
            nonlocal max_path
            if not node:
                return 0
            # Add gain from left subtree
            gain_from_left = max(gain_from_subtree(node.left), 0)
            # Add gain from right subtree
            gain_from_right = max(gain_from_subtree(node.right), 0)
            max_path = max(max_path, gain_from_left + gain_from_right + node.val)
            # Return max sum for a path starting at the root of subtree
            return max(gain_from_left+node.val, gain_from_right+node.val)

        gain_from_subtree(root)
        return max_path

# Main section
for arr_btree in [
                    '[-2,-3,5,2,-1,1,2]',
                 ]:
    print(f'arr_btree = {arr_btree}')
    root = deserialize(arr_btree)
    sol = Solution()
    r = sol.maxPathSum(root)
    print(f'r = {r}')
    print('===========================')

