# ===============================================================
# The N-ary tree class based on Leetcode's array structure.
# ===============================================================
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

class BinaryTree:
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
        return res
    
def deserialize(string):
    print(f'\t>>> string = {string}')
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    print(f'\t>>> nodes = {nodes}')
    kids = nodes[::-1]
    print(f'\t>>> kids = {kids}')
    root = kids.pop()
    print(f'\t>>> root = {root}')
    for node in nodes:
        print(f'\t\t>>> node = {node}')
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

# Main section
#arr_btree = '[1,2,3,4,5,6,null]'
#arr_btree = '[1,2,3,null,4,null,5,6,null,null,7,8,null]'
arr_btree = '[1,2,3,null,4,null,5,6,null,null,7,null,null,8,null]'
root = deserialize(arr_btree)
bt = BinaryTree()
retval = bt.traverseInOrder(root)
print(f'{retval}')

