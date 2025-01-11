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
    if string == '{}':
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
    def traverseTree(self, node, hsh):
        if node:
            if node.left:
                self.traverseTree(node.left, hsh)
            hsh[node.val] = hsh.get(node.val, 0) + 1
            if node.right:
                self.traverseTree(node.right, hsh)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # :type root: TreeNode
        # :rtype List[int]
        res = []
        hsh = dict()
        self.traverseTree(root, hsh)
        #print(hsh)
        for k in sorted(hsh, key=lambda x: hsh[x], reverse=True):
            if len(res) == 0:
                res.append(k)
                max = hsh[k]
            elif hsh[k] == max:
                res.append(k)
            else:
                break
        return res

# Main section
# Note: Binary Search Tree - the Inorder Traversal should result in a sorted node list
for arr_btree in [
                    '[1,null,2,2]',
                    '[0]',
                    '[3,9,20,null,null,20,20]',
                    '[3,1,20,null,null,18,22]',
                    '[11,4,21,1,7,15,29]',
                    '[11,4,19,4,4,19,19]',
                 ]:
    print(f'arr_btree = {arr_btree}')
    root = deserialize(arr_btree)
    sol = Solution()
    r = sol.findMode(root)
    print(f'r = {r}')
    print('===========================')

