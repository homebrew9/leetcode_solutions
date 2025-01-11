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

#class Solution:
#    def isValidBST(self, root: Optional[TreeNode]) -> bool:
#        def dfs(node, val, res):
#            print(f'\tnode, val, res = {node}, {val}, {res}')
#            if node:
#                if node.left:
#                    dfs(node.left, node.val, res)
#                if node.val <= val:
#                    res.append(False)
#                else:
#                    res.append(True)
#                if node.right:
#                    dfs(node.right, node.val, res)
#
#        res = []
#        dfs(root, root.val, res)
#        print(res)
#        return all(res)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.tnode = None
        self.lca_found = False
        def dfs(node):
            if node:
                if p <= node.val <= q:
                    if not self.lca_found:
                        self.tnode = node
                        self.lca_found = True
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)

        if p > q:
            p, q = q, p
        dfs(root)
        #print(f'\ttnode, tnode.val = {tnode}, {tnode.val}')
        return self.tnode

# Main section
for arr_btree, p, q in [
                          #('[6,2,8,0,4,7,9,null,null,3,5]', 2, 8),
                          #('[6,2,8,0,4,7,9,null,null,3,5]', 2, 4),
                          #('[6,2,8,0,4,7,9,null,null,3,5]', 0, 9),
                          #('[6,2,8,0,4,7,9,null,null,3,5]', 0, 5),
                          #('[6,2,8,0,4,7,9,null,null,3,5]', 7, 9),
                          #('[6,2,8,0,4,7,9,null,null,3,5]', 0, 3),
                          ('[2,1]', 2, 1),
                       ]:
    print(f'arr_btree = {arr_btree} ; (p, q) = ({p}, {q})')
    root = deserialize(arr_btree)
    sol = Solution()
    r = sol.lowestCommonAncestor(root, p, q)
    print(f'r = {r}')
    print('===========================')

