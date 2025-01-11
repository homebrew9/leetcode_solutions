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
    #def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
    #    def dfs(node):
    #        if node:
    #            dfs(node.left)
    #            if node.val < self.min_val:
    #                self.min_val = node.val
    #            if node.val > self.max_val:
    #                self.max_val = node.val
    #            dfs(node.right)
    #    
    #    self.min_val, self.max_val = root.val, root.val
    #    dfs(root.left)
    #    diff1 = self.max_val - self.min_val
    #    self.min_val, self.max_val = root.val, root.val
    #    dfs(root.right)
    #    diff2 = self.max_val - self.min_val
    #    return max(diff1, diff2)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def helper(node, cur_max, cur_min):
            if node:
                print(f'\tnode.val, cur_max, cur_min = {node.val}, {cur_max}, {cur_min}')
            else:
                print(f'\tnode.val, cur_max, cur_min = NONE, {cur_max}, {cur_min}')
            # leaf node
            if not node:
                return cur_max - cur_min
            # else update cur_max/cur_min and return the max
            # of left and right subtrees
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = helper(node.left, cur_max, cur_min)
            right = helper(node.right, cur_max, cur_min)
            return max(left, right)

        return helper(root, root.val, root.val)

# Main section
for arr_btree in [
                    '[2,4,3,1,null,0,5,null,6,null,null,null,7]',
                 ]:
    print(f'arr_btree = {arr_btree}')
    root = deserialize(arr_btree)
    sol = Solution()
    r = sol.maxAncestorDiff(root)
    print(f'r = {r}')
    print('===========================')

