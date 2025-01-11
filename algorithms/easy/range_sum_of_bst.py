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

# Main section
for arr_btree, low, high in [
                               ('[10,5,15,3,7,null,18]', 7, 15),
                               ('[10,5,15,3,7,13,18,1,null,6]', 6, 10),
                            ]:
    print(f'arr_btree, low, high = {arr_btree}, {low}, {high}')
    root = deserialize(arr_btree)
    sol = Solution()
    r = sol.rangeSumBST(root, low, high)
    print(f'r = {r}')
    print('===========================')


