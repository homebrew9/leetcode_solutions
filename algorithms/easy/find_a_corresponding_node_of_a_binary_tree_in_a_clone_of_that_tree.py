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

def fetchNode(root, val):
    def dfs(node, val):
        global tgtNode
        print(f'\tIn fetchNode; node, val = {node}, {val}')
        if node:
            if node.left:
                dfs(node.left, val)
            print(f'\t\tnode.val, val = {node.val}, {val}')
            if node.val == val:
                print(f'\t\t\tINSIDE node.val == val')
                print(f'\t\t\tnode, node.val == {node}, {node.val}')
                tgtNode = node
                return
            if node.right:
                dfs(node.right, val)
    tgtNode = None
    dfs(root, val)
    print(f'\ttgtNode = {tgtNode}')
    print(f'\tval     = {tgtNode.val}')
    return tgtNode

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node1, node2, target):
            if node1:
                if node1.left:
                    dfs(node1.left, node2.left, target)
                if node1 == target:
                    return node2
                if node2.right:
                    dfs(node1.right, node2.right, target)
        return dfs(original, cloned, target)

# Main section
for arr1, arr2, target in [
                             ('[7,4,3,null,null,6,19]','[7,4,3,null,null,6,19]',3),
                          ]:
    print(f'arr1, arr2, target = {arr1}, {arr2}, {target}')
    root1 = deserialize(arr1)
    print(f'root1 = {root1}')
    targetNode = fetchNode(root1, target)
    print(f'targetNode = {targetNode}')
    #sol = Solution()
    #r = sol.getTargetCopy(root1, root2, targetNode)
    #print(f'r = {r}')
    print('===========================')

