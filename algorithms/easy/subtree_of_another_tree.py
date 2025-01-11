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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # Try to not use an extra array, for O(1) space complexity
        def dfs(node):
            if node.left:
                dfs(node.left)
            if self.pre is not None:
                self.min_val = min(self.min_val, node.val - self.pre)
            self.pre = node.val
            if node.right:
                dfs(node.right)

        self.min_val = float('inf')
        self.pre = None
        dfs(root)
        return self.min_val

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(s, t):
            #print(f'\t\t\ts, t = {s}, {t}')
            if s is None and t is None:
                return True
            if s is not None and t is not None and s.val == t.val:
                return isIdentical(s.left, t.left) and isIdentical(s.right, t.right)
            return False

        def dfs(node):
            if node:
                #print(f'\tnode = {node}')
                dfs(node.left)
                ret = isIdentical(node, subRoot)
                #print(f'\tret = {ret}')
                if ret:
                    self.is_subtree = True
                dfs(node.right)
                #print(f'\t=====')

        self.is_subtree = False
        dfs(root)
        return self.is_subtree

# Main section
for arr1, arr2 in [
                     #('[3,4,5,1,2]', '[4,1,2]'),
                     ('[3,4,5,1,2,null,null,null,null,0]', '[4,1,2]'),
                  ]:
    print(f'arr1, arr2 = {arr1}, {arr2}')
    root1 = deserialize(arr1)
    root2 = deserialize(arr2)
    sol = Solution()
    r = sol.isSubtree(root1, root2)
    print(f'r = {r}')
    print('===========================')

