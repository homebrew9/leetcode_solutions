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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, res):
            if node:
                res += node.val
                #print(f'\tres = {res} ; node.left, node.right = {node.left}, {node.right}')
                if node.left is None and node.right is None and res == targetSum:
                    #print(f'\tYES!!!')
                    return True
                return dfs(node.left, res) or dfs(node.right, res) or False

        if root is None:
            return False
        ans = dfs(root, 0)
        return ans

# Main section
for arr_btree, targetSum in [
                               ('[5,4,8,11,null,13,4,7,2,null,null,null,1]', 22),
                               ('[1,2,3]', 5),
                               ('[]', 0),
                            ]:
    print(f'arr_btree = {arr_btree}')
    root = deserialize(arr_btree)
    sol = Solution()
    r = sol.hasPathSum(root, targetSum)
    print(f'r = {r}')
    print('===========================')


