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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative function
        # https://faculty.cs.niu.edu/~mcmahon/CS241/Notes/Data_Structures/binary_tree_traversals.html
        stack = list()
        res = list()
        last_visited = None
        p = root
        while p and last_visited != root:
            # Go all the way to the left
            while p and p != last_visited:
                stack.append(p)
                p = p.left
            # p might be None at this point; backtrack one level
            p = stack.pop()
            if p.right is None or p.right == last_visited:
                # Either the node has no right child, or we have traversed
                # its right subtree. In either case, visit it.
                res += [p.val]
                last_visited = p
            else:
                # We've got some work to do; visit the right subtree
                stack.append(p)
                p = p.right
        return res

for s in [
            '[1,null,2,3]',
            '[]',
            '[1]',
            '[1,2]',
            '[1,2,3]',
            '[1,2,3,4,5,6,7]',
            '[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]',
         ]:
    print(f's = {s}')
    root = deserialize(s)
    print(f'root = {root} => {serialize(root)}')
    sol = Solution()
    r = sol.postorderTraversal(root)
    print(f'r = {r}')
    print('===================')


