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

def serialize(root):
    def dfs(node):
        global res
        if node:
            res += f'({node.val}'
            if not node.left and node.right:
                res += '()'
                dfs(node.right)
            elif not node.right and node.left:
                dfs(node.left)
                res += '()'
            else:
                dfs(node.left)
                dfs(node.right)
            res += f')'
    global res
    res = ''
    dfs(root)
    return res

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node:
                if node.val in (p.val, q.val):
                    return node
                left_val = dfs(node.left)
                right_val = dfs(node.right)
                if left_val is None and right_val is None:
                    return None
                if left_val is not None and right_val is not None:
                    return node
                if left_val is not None:
                    return left_val
                if right_val is not None:
                    return right_val
        tmp = dfs(root)
        return tmp

# Main section
for arr_btree, pval, qval in [
                                ('[3,5,1,6,2,0,8,null,null,7,4]', 5, 1),
                                ('[3,5,1,6,2,0,8,null,null,7,4]', 5, 4),
                                ('[1,2,3,4,5,6,7,8,null,null,9,null,null,10,11,12,13,14,null,15,null,16,17,null,null,null,18,null,null,19,null,20,null,21,null,22,23,null,null,24,null,null,25]', 22, 25),
                                ('[1,2,3,4,5,6,7,8,null,null,9,null,null,10,11,12,13,14,null,15,null,16,17,null,null,null,18,null,null,19,null,20,null,21,null,22,23,null,null,24,null,null,25]', 19, 21),
                                ('[1,2,3,4,5,6,7,8,null,null,9,null,null,10,11,12,13,14,null,15,null,16,17,null,null,null,18,null,null,19,null,20,null,21,null,22,23,null,null,24,null,null,25]', 23, 8),
                                ('[1,2,3,4,5,6,7,8,null,null,9,null,null,10,11,12,13,14,null,15,null,16,17,null,null,null,18,null,null,19,null,20,null,21,null,22,23,null,null,24,null,null,25]', 9, 4),
                                ('[1,2,3,4,5,6,7,8,null,null,9,null,null,10,11,12,13,14,null,15,null,16,17,null,null,null,18,null,null,19,null,20,null,21,null,22,23,null,null,24,null,null,25]', 25, 12),
                                ('[1,2,3,4,5,6,7,8,null,null,9,null,null,10,11,12,13,14,null,15,null,16,17,null,null,null,18,null,null,19,null,20,null,21,null,22,23,null,null,24,null,null,25]', 12, 2),
                                ('[1,2,3,4,5,6,7,8,null,null,9,null,null,10,11,12,13,14,null,15,null,16,17,null,null,null,18,null,null,19,null,20,null,21,null,22,23,null,null,24,null,null,25]', 6, 18),
                             ]:
    print(f'arr_btree, pval, qval = {arr_btree}, {pval}, {qval}')
    root = deserialize(arr_btree)
    p = TreeNode(pval)
    q = TreeNode(qval)
    sol = Solution()
    r = sol.lowestCommonAncestor(root, p, q)
    print(f'r, rval = {r}, {r.val}')
    print('===========================')


