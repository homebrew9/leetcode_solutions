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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node, val):
            #print(node.val, val)
            if node is not None and node.val == val:
                return node
            if node.left:
                ptr = dfs(node.left, val)
                if ptr is not None:
                    return ptr
            if node.right:
                ptr = dfs(node.right, val)
                if ptr is not None:
                    return ptr
        new_head = dfs(root, val)
        return new_head

# Main section
for btree, val in [
                     ('[4,2,7,1,3]', 2),
                     ('[4,2,7,1,3]', 5),
                     ('[18,2,22,null,null,null,63,null,84,null,null]', 63),
                  ]:
    print(f'btree, val = {btree}, {val}')
    root = deserialize(btree)
    print(f'root = {root}')
    sol = Solution()
    r = sol.searchBST(root, val)
    print(f'r = {r}')
    print('==========================')

