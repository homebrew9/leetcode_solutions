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
    def __init__(self):
        # A problem constraint is that the number of nodes is [0, 10^5]
        # The max height would typically be log(10^5), but we can go
        # higher as a "starter" value for min_depth.
        self.min_depth = 100000

    def traverseInOrderHelper(self, node, depth):
        if node:
            depth += 1
            # If we are at leaf node then update min_depth
            if not node.left and not node.right:
                self.min_depth = min(self.min_depth, depth)
            if node.left:
                self.traverseInOrderHelper(node.left, depth)
            if node.right:
                self.traverseInOrderHelper(node.right, depth)
            depth -= 1

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 0
        self.traverseInOrderHelper(root, depth)
        return self.min_depth


# Main section
for btree in [
                ('3,9,20,null,null,15,7]'),
                ('[2,null,3,null,4,null,5,null,6]'),
                ('[]'),
                ('[1]'),
             ]:
    print(f'btree = {btree}')
    root = deserialize(btree)
    sol = Solution()
    r = sol.minDepth(root)
    print(f'r = {r}')
    print('===========================')



