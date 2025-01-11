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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root

# Main section
for arr_btree, p, q in [
                          ('[6,2,8,0,4,7,9,null,null,3,5]', TreeNode(2), TreeNode(8)),
                          ('[6,2,8,0,4,7,9,null,null,3,5]', TreeNode(2), TreeNode(4)),
                          ('[6,2,8,0,4,7,9,null,null,3,5]', TreeNode(0), TreeNode(9)),
                          ('[6,2,8,0,4,7,9,null,null,3,5]', TreeNode(0), TreeNode(5)),
                          ('[6,2,8,0,4,7,9,null,null,3,5]', TreeNode(7), TreeNode(9)),
                          ('[6,2,8,0,4,7,9,null,null,3,5]', TreeNode(0), TreeNode(3)),
                          ('[2,1]', TreeNode(2), TreeNode(1)),
                       ]:
    print(f'arr_btree = {arr_btree} ; (p, q) = ({p}, {q})')
    root = deserialize(arr_btree)
    sol = Solution()
    r = sol.lowestCommonAncestor(root, p, q)
    print(f'r = {r}')
    print('===========================')


