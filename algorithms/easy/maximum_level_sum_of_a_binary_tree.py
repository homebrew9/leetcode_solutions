#
# We use BFS or level order traversal to solve this problem.
#
import btree as bt
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[bt.TreeNode]) -> int:
        dq = deque()
        dq.append(root)
        max_sum = float('-inf')
        curr_sum = 0
        res, level = 0, 0
        while dq:
            N = len(dq)
            curr_sum = 0
            level += 1
            for _ in range(N):
                cur = dq[0]
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
                curr_sum += dq.popleft().val
            #print(f'\tlevel, curr_sum, max_sum = {level}, {curr_sum}, {max_sum}')
            if curr_sum > max_sum:
                max_sum = curr_sum
                res = level
        return res

# Main section
for arr_btree in [
                    '[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]',
                    '[1,2,89,4,5,6,7,8,9,10,11,12,13,14,15]',
                    '[1,2,90,4,5,6,7,8,9,10,11,12,13,14,15]',
                    '[1,2,91,4,5,6,7,8,9,10,11,12,13,14,15]',
                    '[1,7,0,7,-8]',
                    '[989,null,10250,98693,-89388,null,null,null,-32127]',
                 ]:
    print(f'arr_btree = {arr_btree}')
    root = bt.deserialize(arr_btree)
    sol = Solution()
    r = sol.maxLevelSum(root)
    print(f'r = {r}')
    print('===========================')

