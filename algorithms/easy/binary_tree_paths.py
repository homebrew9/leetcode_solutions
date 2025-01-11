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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.Bal = True
        self.indent = 0
        def dfs(node):
            self.indent += 1
            indent = '  '*self.indent
            #print(f'{indent}node = {node}')
            if not node:
                return 0
            lft = dfs(node.left)
            rgt = dfs(node.right)
            #print(f'{indent}lft, rgt = {lft}, {rgt}')
            if abs(lft - rgt) > 1:
                self.Bal = False
            return max(lft, rgt) + 1
        dfs(root)
        return self.Bal

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.leftSum = 0
        def inorderTraversal(node):
            if node:
                if node.left:
                    # If the left node is a leaf, then update leftSum
                    if node.left.left == None and node.left.right == None:
                        self.leftSum += node.left.val
                    inorderTraversal(node.left)
                print(node.val)
                if node.right:
                    inorderTraversal(node.right)
        inorderTraversal(root)
        return self.leftSum

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.arr = list()
        def preorderTraversal(node, s):
            if node:
                s += str(node.val) + '->'
                #print(s)
                if node.left == None and node.right == None:
                    s = s.rstrip('->')
                    self.arr.append(s)
                preorderTraversal(node.left, s)
                preorderTraversal(node.right, s)
        s = ''
        preorderTraversal(root, s)
        return self.arr

# Main section
for btree in [
                ('[1,2,3,null,5]'),
                ('[1]'),
                ('[3,9,20,null,null,15,7]'),
                ('[1,2,2,3,3,null,null,4,4]'),
                ('[1,2,2,3,null,null,3,4,null,null,4]'),
             ]:
    print(f'btree = {btree}')
    root = deserialize(btree)
    sol = Solution()
    r = sol.binaryTreePaths(root)
    print(f'r = {r}')
    print('===========================')

