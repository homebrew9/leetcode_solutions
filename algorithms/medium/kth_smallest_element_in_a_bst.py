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

import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if node:
                dfs(node.left)
                heapq.heappush(self.h, -node.val)
                if len(self.h) > k:
                    heapq.heappop(self.h)
                dfs(node.right)
        self.h = []
        heapq.heapify(self.h)
        dfs(root)
        tmp = -heapq.heappop(self.h)
        return tmp

    def kthSmallest_1(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if node:
                dfs(node.left)
                if len(self.arr) < k:
                    self.arr.append(node.val)
                dfs(node.right)
        self.arr = []
        dfs(root)
        return self.arr[-1]

# Main section
for arr_btree, k in [
                       ('[3,1,4,null,2]', 1),
                       ('[5,3,6,2,4,null,null,1]', 3),
                       ('[4,2,5,1,3,null,6]', 5),
                    ]:
    print(f'arr_btree, k = {arr_btree}, {k}')
    root = deserialize(arr_btree)
    sol = Solution()
    r1 = sol.kthSmallest(root, k)
    r2 = sol.kthSmallest_1(root, k)
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print('===========================')


