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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # Try to not use an extra array, for O(1) space complexity
        def dfs(node):
            if node.left:
                dfs(node.left)
            if self.pre is not None:
                self.min_val = min(self.min_val, node.val - self.pre)
            self.pre = node.val
            if node.right:
                dfs(node.right)

        self.min_val = float('inf')
        self.pre = None
        dfs(root)
        return self.min_val

# Main section
for arr_btree in [
                    '[4,2,6,1,3]',
                    '[1,0,48,null,null,12,49]',
                    '[0,null,2236,1277,2776,519]',
                 ]:
    print(f'arr_btree = {arr_btree}')
    root = deserialize(arr_btree)
    sol = Solution()
    r = sol.minDiffInBST(root)
    print(f'r = {r}')
    print('===========================')

