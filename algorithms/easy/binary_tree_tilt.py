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
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(node, total):
            if not node:
                return 0
            if node:
                left = dfs(node.left, total)
                right = dfs(node.right, total)
                #print(f'\tnode, node.val, left, right = {node}, {node.val}, {left}, {right}')
                self.total += abs(left - right)
                #print(f'\t\tself.total = {self.total}')
                return total + left + right + node.val

        self.total = 0
        dfs(root, 0)
        return self.total

# Main section
for arr_btree in [
                    '[1,2,3]',
                    '[4,2,9,3,5,null,7]',
                    '[21,7,14,1,1,2,2,3,3]',
                 ]:
    print(f'arr_btree = {arr_btree}')
    root = deserialize(arr_btree)
    sol = Solution()
    r = sol.findTilt(root)
    print(f'r = {r}')
    print('===========================')

