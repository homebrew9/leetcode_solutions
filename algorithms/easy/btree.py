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
#    def traverseInOrderHelper(self, node, res):
#        if node:
#            if node.left:
#                self.traverseInOrderHelper(node.left, res)
#            res.append(node.val)
#            if node.right:
#                self.traverseInOrderHelper(node.right, res)
#
#    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#        res = []
#        self.traverseInOrderHelper(root, res)
#        return res
#
## Main section
#for arr_btree in [
#                    '[1,null,2,3]',
#                    '[]',
#                    '[1]',
#                 ]:
#    print(f'arr_btree = {arr_btree}')
#    root = deserialize(arr_btree)
#    sol = Solution()
#    r = sol.inorderTraversal(root)
#    print(f'r = {r}')
#    print('===========================')
#

