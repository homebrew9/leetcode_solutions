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

#class Solution:
#    def traverseInOrderHelper(self, node, res):
#        if node:
#            if node.left:
#                self.traverseInOrderHelper(node.left, res)
#            res.append(node.val)
#            if node.right:
#                self.traverseInOrderHelper(node.right, res)
#
#    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#        res = []
#        self.traverseInOrderHelper(root, res)
#        return res

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def dfs(node, res):
            if node:
                if node.left:
                    dfs(node.left, res)
                res.append(node.val)
                if node.right:
                    dfs(node.right, res)

        def bsearch(arr, num):
            left, right = 0, len(arr) - 1
            while left < right:
                mid = (left + right)//2
                if arr[mid] == num:
                    return mid
                elif arr[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        res = []
        dfs(root, res)
        #print(f'\t>> res = {res}')
        ans = []
        for q in queries:
            ind = bsearch(res, q)
            #print(f'\tq, ind = {q}, {ind}')
            if res[ind] == q:
                ans.append([res[ind], res[ind]])
            elif res[ind] < q:
                if ind == len(res) - 1:
                    ans.append([res[ind], -1])
                else:
                    ans.append([res[ind], res[ind+1]])
            elif res[ind] > q:
                if ind == 0:
                    ans.append([-1, res[ind]])
                else:
                    ans.append([res[ind-1], res[ind]])
        return ans

# Main section
for arr_btree, queries in [
                             ('[6,2,13,1,4,9,15,null,null,null,null,null,null,14]', [2,5,16]),
                             ('[4,null,9]', [3]),
                          ]:
    print(f'arr_btree, queries = {arr_btree}, {queries}')
    root = deserialize(arr_btree)
    sol = Solution()
    r = sol.closestNodes(root, queries)
    print(f'r = {r}')
    print('===========================')

