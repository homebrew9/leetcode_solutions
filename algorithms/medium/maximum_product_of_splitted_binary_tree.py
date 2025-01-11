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
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def btreeSum(node):
            if node:
                btreeSum(node.left)
                self.total += node.val
                btreeSum(node.right)

        def dfs(node):
            if not node:
                return 0
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                subtree_sum = left + right + node.val
                print(f'\t\tnode, left, right, subtree_sum, comp_sum = {node}, {left}, {right}, {subtree_sum}, {self.total - subtree_sum}')
                if (self.total - subtree_sum) * subtree_sum > self.max_prod:
                    self.max_prod = (self.total - subtree_sum) * subtree_sum
                return left + right + node.val

        self.total = 0
        self.max_prod = 0
        btreeSum(root)
        print(f'\ttotal = {self.total}')
        dfs(root)
        return self.max_prod % (10**9 + 7)

# Main section
for arr_btree in [
                    '[1,2,3,4,5,6]',
                    '[1,null,2,3,4,null,null,5,6]',
                 ]:
    print(f'arr_btree = {arr_btree}')
    root = deserialize(arr_btree)
    sol = Solution()
    r = sol.maxProduct(root)
    print(f'r = {r}')
    print('===========================')

