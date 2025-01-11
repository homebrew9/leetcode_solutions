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
    def traverseInOrderHelper(self, node1, node2):
        print(f'\t(node1, node2) = ({node1}, {node2})')
        # Both are NULL
        if not node1 and not node2:
            return True
        # Only one is NULL
        if not node1 or not node2:
            return False
        # Both are NON-NULL and their values are different
        if node1.val != node2.val:
            return False
        return self.traverseInOrderHelper(node1.left, node2.right) and \
               self.traverseInOrderHelper(node1.right, node2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.traverseInOrderHelper(root.left, root.right)


# Main section
for btree in [
                ('[1,2,2,3,4,4,3]'),
                ('[1,2,2,null,3,null,3]')
             ]:
    print(f'btree = {btree}')
    root = deserialize(btree)
    sol = Solution()
    r = sol.isSymmetric(root)
    print(f'r = {r}')
    print('===========================')


