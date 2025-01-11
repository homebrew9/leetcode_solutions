





        

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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.range_sum = 0

        def dfs(node, low, high):
            if node:
                if node.left:
                    dfs(node.left, low, high)
                if low <= node.val <= high:
                    self.range_sum += node.val
                if node.right:
                    dfs(node.right, low, high)

        dfs(root, low, high)
        return self.range_sum

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, res):
            if node:
                if node.left:
                    dfs(node.left, res)
                # If we are at the leaf node, then add its value to the array
                if not node.left and not node.right:
                    res += [node.val]
                if node.right:
                    dfs(node.right, res)

        res1, res2 = list(), list()
        dfs(root1, res1)
        dfs(root2, res2)
        return res1 == res2

# Main section
for arr_btree1, arr_btree2 in [
                                 ('[3,5,1,6,2,9,8,null,null,7,4]', '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'),
                                 ('[1,2,3]', '[1,3,2]'),
                              ]:
    print(f'arr_btree1, arr_btree2 = {arr_btree1}, {arr_btree2}')
    root1 = deserialize(arr_btree1)
    root2 = deserialize(arr_btree2)
    sol = Solution()
    r = sol.leafSimilar(root1, root2)
    print(f'r = {r}')
    print('===========================')

