from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque, defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS works for this problem. The row value is not really required.
        if not root:
            return list()
        hsh = defaultdict(list)
        dq = deque()
        dq.append((0, root))
        while dq:
            size = len(dq)
            for _ in range(size):
                col, node = dq.popleft()
                hsh[col] += [node.val]
                if node.left:
                    dq.append((col - 1, node.left))
                if node.right:
                    dq.append((col + 1, node.right))
        return [hsh[k] for k in sorted(hsh)]

# Main section
# [3,9,20,null,null,15,7]
# [3,9,8,4,0,1,7]
# [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]





