from typing import List, Optional
import bisect

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def dfs(node, arr):
            if node:
                dfs(node.left, arr)
                arr.append(node.val)
                dfs(node.right, arr)
        res1 = list()
        dfs(root1, res1)
        res2 = list()
        dfs(root2, res2)
        for n in res1:
            delta = target - n
            idx = bisect.bisect_right(res2, delta)
            if idx == 0:
                if res2[idx] == delta:
                    return True
            elif idx > 0:
                if res2[idx-1] == delta:
                    return True
        return False

# Main section
#  root1, root2, target = [2,1,4], [1,0,3], 5          => Output = True
#  root1, root2, target = [0,-10,10], [5,1,7,0,2], 18  => Output = False
#
































