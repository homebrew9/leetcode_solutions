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
    def postorderTraversalRec(self, root: Optional[TreeNode]) -> List[int]:
        def postorderTraversalHelper(node, res):
            if node:
                if node.left:
                    postorderTraversalHelper(node.left, res)
                if node.right:
                    postorderTraversalHelper(node.right, res)
                res.append(node.val)
        res = []
        postorderTraversalHelper(root, res)
        return res
    def postorderTraversalItr(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative Postorder Traversal using one stack and last_visited pointer
        p = root
        last_visited = None
        stack = list()
        res = list()
        while p and last_visited != root:
            while p and last_visited != p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            if not p.right or p.right == last_visited:
                res.append(p.val)
                last_visited = p
            else:
                stack.append(p)
                p = p.right
        return res
    def postorderTraversalItr_1(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative Postorder Traversal using one stack with reversal at end
        stack = list()
        res = list()
        if root:
            stack.append(root)
        while stack:
            p = stack.pop()
            res.append(p.val)
            if p.left:
                stack.append(p.left)
            if p.right:
                stack.append(p.right)
        return res[::-1]

# Main section
for btree in [
                ('[1,null,2,3]'),
                ('[]'),
                ('[1]'),
                ('[4,2,6,1,3,5,7]'),
                ('[1,2,3,4,5,6,7]'),
                ('[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]'),
             ]:
    print(f'btree = {btree}')
    root = deserialize(btree)
    sol = Solution()
    r1 = sol.postorderTraversalRec(root)
    print(f'r1    = {r1}')
    r2 = sol.postorderTraversalItr(root)
    print(f'r2    = {r2}')
    r3 = sol.postorderTraversalItr_1(root)
    print(f'r3    = {r3}')
    print('===========================')


