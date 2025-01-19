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

def serialize(root):
    def dfs(node):
        global res
        if node:
            res += f'({node.val}'
            if not node.left and node.right:
                res += '()'
                dfs(node.right)
            elif not node.right and node.left:
                dfs(node.left)
                res += '()'
            else:
                dfs(node.left)
                dfs(node.right)
            res += f')'
    global res
    res = ''
    dfs(root)
    return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def bfs(node):
            arr = list()
            dq = deque([node])
            while dq:
                for _ in range(len(dq)):
                    curr = dq.popleft()
                    arr.append(curr.val if curr else None)
                    if not curr:
                        continue
                    if curr.left:
                        dq.append(curr.left)
                    else:
                        dq.append(None)
                    if curr.right:
                        dq.append(curr.right)
                    else:
                        dq.append(None)
            i = len(arr) - 1
            while i >= 0:
                if arr[i] is None and arr[i-1] is None:
                    arr.pop()
                    arr.pop()
                else:
                    break
                i -= 2
            return ','.join(['null' if x is None else str(x) for x in arr])
        if not root:
            return ''
        return bfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        if ',' not in data:
            return TreeNode(int(data))
        arr = [None if x == 'null' else TreeNode(int(x)) for x in data.split(',')]
        root = arr[0]
        N = len(arr)
        i, j = 0, 1
        while j < N:
            while arr[i] is None:
                i += 1
            arr[i].left = arr[j]
            j += 1
            if j >= N:
                return root
            arr[i].right = arr[j]
            j += 1
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# Main section
for s in [
            #'[1,2,3,4,5,6,7]',
            #'[3,9,20,null,null,15,7]',
            #'[7,3,10,1,4,null,12]',
            #'[7,9,null,3,null,1,null]',
            #'[8,null,9,null,10,null,11]',
            #'[1,null,2,null,3,4,5,6,null,7,null]',
            #'[1,2,null,3,null,4,5,null,null,null,6,7,8,9,null,null,10]',
            #'[1]',
            #'[1,2]',
            #'[1,null,2]',
            #'[1,2,3]',
            '[]',
         ]:
    print(f's = {s}')
    root = deserialize(s)
    print(f'root = {root}')
    ser = Codec()
    ret = ser.serialize(root)
    print(f'ret = {ret}')
    deser = Codec()
    ans = deser.deserialize(ret)
    print(f'ans = {ans} => {serialize(ans)} => {serialize(root)}')

    # ser = Codec()
    # deser = Codec()
    # tmp = ser.serialize(root)
    # ans = deser.deserialize(tmp)
    # print(f'ans = {ans} => {serialize(ans)}')

    # root = deserialize(s)
    # r = sol.connect(root)
    # print(f'r = {r} => {serialize(r)}')
    print('===========================')

