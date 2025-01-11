from typing import Optional
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
    def traverseInOrderHelper(self, node, res):
        if node:
            if node.left:
                self.traverseInOrderHelper(node.left, res)
            res.append(node.val)
            if node.right:
                self.traverseInOrderHelper(node.right, res)

    def traverseInOrder(self, root):
        # :type root: TreeNode
        # :rtype List[int]
        res = []
        self.traverseInOrderHelper(root, res)
        print(res)
        min_diff = abs(res[1] - res[0])
        for i in range(2,len(res)):
            min_diff = min(min_diff, abs(res[i] - res[i-1]))
        return min_diff

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        retval = self.traverseInOrder(root)
        #print(retval)
        return retval

# Main section
for arr_btree in [
                    '[4,2,6,1,3]',
                    '[1,0,48,null,null,12,49]',
                    '[3,1,null]',
                 ]:
    print(f'arr_btree = {arr_btree}')
    root = deserialize(arr_btree)
    sol = Solution()
    r = sol.getMinimumDifference(root)
    print(f'r = {r}')
    print('===========================')

