from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# I haven't figured out the deserialization method for N-ary trees yet.
# So I will try to construct the tree manually for this script.
# The code is by User: hiepit, and I have studied it thoroughly.

class Node:
    children = list()
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.children = children
    def __repr__(self):
        return 'Node({})'.format(self.val)

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def dfs(root, level):
            if root == None:
                return
            if level == len(ans):
                ans.append([])
            ans[level].append(root.val)
            for child in root.children:
                dfs(child, level+1)

        ans = []
        dfs(root, 0)
        return ans

# Main section
sol = Solution()
root = Node(1, [Node(3), Node(2), Node(4)])
res = sol.levelOrder(root)
print(res)

