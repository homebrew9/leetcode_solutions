#
# Does not work for a case like this: [1, 2]
# The output should be [1, null, 2] but this code returns [1,2]
#
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
        self.arr = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, res):
            if node:
                #print(f'\tnode.val = {node.val}')
                res.append(node.val)
                if node.left == None and node.right == None:
                    #print(f'\t\tres = {res} ; sum = {sum(res)}')
                    if sum(res) == targetSum:
                        self.arr.append(copy.deepcopy(res))
                if node.left:
                    dfs(node.left, res)
                if node.right:
                    dfs(node.right, res)
                res.pop()
        res = []
        dfs(root, res)
        return self.arr

class Solution:
    def __init__(self):
        self.hsh = dict()

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if node:
                #print(f'\tval = {node.val}, depth = {depth}')
                if depth in self.hsh:
                    self.hsh[depth].append(node.val)
                else:
                    self.hsh[depth] = [node.val]
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
            else:
                if depth in self.hsh:
                    self.hsh[depth].append(None)
                else:
                    self.hsh[depth] = [None]

        def invert(node, depth):
            if node:
                node.val = self.hsh[depth].pop()
                invert(node.left, depth + 1)
                invert(node.right, depth + 1)

        if root is None:
            return None
        dfs(root, 1)
        print(f'hsh = {self.hsh}')
        invert(root, 1)
        print(f'hsh = {self.hsh}')
        return root

# Main section
for btree in [
                #'[4,2,7,1,3,6,9]',
                #'[2,1,3]',
                #'[]',
                '[1,2]',
             ]:
    print(f'btree = {btree}')
    root = deserialize(btree)
    sol = Solution()
    r = sol.invertTree(root)
    print(f'r = {r}')
    print('===========================')

