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

def serialize(root):
    def dfs(node):
        global res
        if node:
            res += f'({node.val}'
            if not node.left and node.right:
                res += '()'
                dfs(node.right)
            elif not node.right and node.left:
                dfs(node.left)
                res += '()'
            else:
                dfs(node.left)
                dfs(node.right)
            res += f')'
    global res
    res = ''
    dfs(root)
    return res

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(arr):
            val = preorder[self.ind]
            node = TreeNode(val)
            idx = arr.index(val)
            left_arr = arr[:idx]
            right_arr = arr[idx+1:]
            if not left_arr or self.ind >= N-1:
                left_tree = None
            else:
                self.ind += 1
                left_tree = build(left_arr)
            if not right_arr or self.ind >= N-1:
                right_tree = None
            else:
                self.ind += 1
                right_tree = build(right_arr)
            node.left = left_tree
            node.right = right_tree
            return node
        N = len(preorder)
        self.ind = 0
        return build(inorder)

# Main section
for preorder, inorder in [
                            ([3,9,20,15,7], [9,3,15,20,7]),
                            ([-1], [-1]),
                            ([1,2], [2,1]),
                            ([1,2], [1,2]),
                            ([1,2,4,3,5], [4,2,1,3,5]),
                            ([1,2,3], [1,3,2]),
                            ([1,2,3,4], [2,4,3,1]),
                         ]:
    print(f'preorder, inorder = {preorder}, {inorder}')
    sol = Solution()
    r = sol.buildTree(preorder, inorder)
    print(f'r = {r} => {serialize(r)}')
    print('===========================')


