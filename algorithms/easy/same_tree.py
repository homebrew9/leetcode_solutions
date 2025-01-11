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
    def traverseInOrderHelper(self, node1, node2):
        #if node:
        #    if node.left:
        #        self.traverseInOrderHelper(node1.left, node2.left)
        #    res.append(node.val)
        #    if node.right:
        #        self.traverseInOrderHelper(node1.right, node2.right)
        print(f'\t(node1, node2) = ({node1}, {node2})')
        # Both are NULL
        if not node1 and not node2:
            return True
        # Only one is NULL
        if not node1 or not node2:
            return False
        # Both are NON-NULL and their values are different
        if node1.val != node2.val:
            return False
        return self.traverseInOrderHelper(node1.left, node2.left) and \
               self.traverseInOrderHelper(node1.right, node2.right)
        # ==============================
        # Why did the following logic not work??? - need to investigate it more thoroughly
        # ==============================
        # #if not (node1 and node2 and node1.val == node2.val):
        # if (node1 and not node2) or (node2 and not node1) or (node1 and node2 and node1.val != node2.val):
        #     print(f'\t\tin if # 1...')
        #     return False
        # if (node1.left and not node2.left) or (node2.left and not node1.left):
        # #if not (node1.left and node2.left):
        #     print(f'\t\tin if # 2...')
        #     print(f'\t\t(node1.left, node2.left) = ({node1.left}, {node2.left})')
        #     return False
        # if node1.left:
        #     return self.traverseInOrderHelper(node1.left, node2.left)
        # if (node1.right and not node2.right) or (node2.right and not node1.right):
        # #if not (node1.right and node2.right):
        #     return False
        # if node1.right:
        #     return self.traverseInOrderHelper(node1.right, node2.right)
        # #return True

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #res1 = []
        #self.traverseInOrderHelper(p, res1)
        #print(res1)
        #res2 = []
        #self.traverseInOrderHelper(q, res2)
        #print(res2)
        #return res1 == res2
        return self.traverseInOrderHelper(p, q)

# Main section
for btree1, btree2 in [
                         ('[1,2,3]', '[1,2,3]'),
                         ('[1,2]', '[1,null,2]'),
                         ('[1,2,1]', '[1,1,2]'),
                         ('[1,1]', '[1,null,1]'),  # <== fails for this
                      ]:
    print(f'btree1 = {btree1}, btree2 = {btree2}')
    root1 = deserialize(btree1)
    root2 = deserialize(btree2)
    sol = Solution()
    r = sol.isSameTree(root1, root2)
    print(f'r = {r}')
    print('===========================')

