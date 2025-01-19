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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(inorder):
            if len(inorder) == 0:
                return None
            root = TreeNode(postorder[self.pos])
            i = inorder.index(postorder[self.pos])
            self.pos -= 1
            right_node = build(inorder[i+1:])
            left_node = build(inorder[:i])
            root.right = right_node
            root.left = left_node
            return root
        self.pos = len(postorder) - 1
        return build(inorder)

# Main section
for inorder, postorder in [
                            ([9,3,15,20,7], [9,15,7,20,3]),
                            ([-1], [-1]),
                            ([4,3,5,9,7,6,8,10,2,1], [4,9,7,10,8,6,5,3,2,1]),
                          ]:
    print(f'inorder, postorder = {inorder}, {postorder}')
    sol = Solution()
    r = sol.buildTree(inorder, postorder)
    print(f'r = {r} => {serialize(r)}')
    print('===========================')


