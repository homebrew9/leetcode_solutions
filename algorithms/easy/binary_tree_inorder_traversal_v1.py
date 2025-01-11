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
    def traverseInOrderHelper(self, node, res):
        if node:
            if node.left:
                self.traverseInOrderHelper(node.left, res)
            res.append(node.val)
            if node.right:
                self.traverseInOrderHelper(node.right, res)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.traverseInOrderHelper(root, res)
        return res
    def inorderTraversal_1(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative DFS traversal using a stack
        res = list()
        stack = list()
        node = root
        while node is not None or len(stack) > 0:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

# Main section
for arr_btree in [
                    '[1,null,2,3]',
                    '[]',
                    '[1]',
                    '[1,2,3,4,5,6,7]',
                    '[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]',
                 ]:
    print(f'arr_btree = {arr_btree}')
    root = deserialize(arr_btree)
    sol = Solution()
    r = sol.inorderTraversal(root)
    print(f'r (DFS recursive) = {r}')
    r1 = sol.inorderTraversal_1(root)
    print(f'r1 (DFS stack)    = {r1}')
    print('===========================')


