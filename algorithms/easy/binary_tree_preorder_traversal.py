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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorderTraversalHelper(node, res):
            if node:
                res.append(node.val)
                if node.left:
                    preorderTraversalHelper(node.left, res)
                if node.right:
                    preorderTraversalHelper(node.right, res)
        res = []
        preorderTraversalHelper(root, res)
        return res

# Main section
for btree in [
                ('[1,null,2,3]'),
                ('[]'),
                ('[1]'),
                ('[4,2,6,1,3,5,7]'),
             ]:
    print(f'btree = {btree}')
    root = deserialize(btree)
    sol = Solution()
    r = sol.preorderTraversal(root)
    print(f'r = {r}')
    print('===========================')

