# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if node:
                dfs(node.left, depth + 1)
                self.hsh[depth] += [node]
                dfs(node.right, depth + 1)
        def reset_tree():
            for k in sorted(self.hsh.keys()):
                if k % 2 == 0:
                    # attach child nodes in reverse order, and then reverse
                    # the order of nodes in the next level!
                    if k + 1 in self.hsh:
                        N, M = len(self.hsh[k]), len(self.hsh[k+1])
                        i, j = 0, M - 1
                        while i < N:
                            self.hsh[k][i].left = self.hsh[k+1][j]
                            j -= 1
                            self.hsh[k][i].right = self.hsh[k+1][j]
                            j -= 1
                            i += 1
                        self.hsh[k+1] = self.hsh[k+1][::-1]
                else:
                    # attach child nodes in original order
                    if k + 1 in self.hsh:
                        N, M = len(self.hsh[k]), len(self.hsh[k+1])
                        i, j = 0, 0
                        while i < N:
                            self.hsh[k][i].left = self.hsh[k+1][j]
                            j += 1
                            self.hsh[k][i].right = self.hsh[k+1][j]
                            j += 1
                            i += 1
        self.hsh = defaultdict(list)
        dfs(root, 0)
        reset_tree()
        return root

# ====================================
# Simpler solution
# ====================================
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, depth):
            if node:
                dfs(node.left, depth + 1)
                if depth % 2 == 1:
                    self.hsh[depth] += [node.val]
                dfs(node.right, depth + 1)
        def reset_tree(node, depth):
            if node:
                reset_tree(node.left, depth + 1)
                if depth % 2 == 1:
                    node.val = self.hsh[depth].pop()
                reset_tree(node.right, depth + 1)
        self.hsh = defaultdict(list)
        dfs(root, 0)
        reset_tree(root, 0)
        return root


