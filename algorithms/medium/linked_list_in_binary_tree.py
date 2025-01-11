from typing import List, Optional
from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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

def deserialize_btree(string):
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

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deserialize_llist(arr, pos=-1):
    if len(arr) == 0:
        return None
    # pos is the index of the node to which the last node of the linked list points.
    # If pos is -1 then the last node does not point to any node
    # If pos is > -1 we save the node while creating the linked list
    head = ListNode(arr[0])
    node = head
    last_ptr = None
    for i in range(1, len(arr)):
        node1 = ListNode(arr[i])
        if i == pos:
            last_ptr = node1
        node.next = node1
        node = node.next
    if pos == 0:
        node.next = head
    else:
        node.next = last_ptr
    return head

def serialize_llist(head):
    arr = []
    # We might hit a cycle in the linked list. If it is not detected, the
    # linked list iteration will go on forever!
    nodeSet = set()
    is_cycle = False
    arr.append(head.val)
    node = head
    nodeSet.add(node)
    while not node.next is None:
        node = node.next
        arr.append(node.val)
        if node in nodeSet:
            is_cycle = True
            break
        nodeSet.add(node)
    if is_cycle:
        return ' -> '.join([str(i) for i in arr]) + ' [Cyclic: aborted]'
    else:
        return ' -> '.join([str(i) for i in arr])

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def isListInBTree(head, node):
            print(f'\t\thead, head.val, node = {head}, {not head or head.val}, {node}')
            if head is None: # and node is None:
                return True
            if (not head and node) or (head and not node):
                return False
            if head and node and head.val != node.val:
                return False
            return isListInBTree(head.next, node.left) or isListInBTree(head.next, node.right)

        def dfs():
            while self.dq:
                node = self.dq.popleft()
                print(f'node, node.val = {node}, {node.val}')
                if node.val == head.val:
                    ret = isListInBTree(head, node)
                    print(f'\tret = {ret}')
                    if ret:
                        return True
                if node.left:
                    self.dq.append(node.left)
                if node.right:
                    self.dq.append(node.right)
            return False

        self.dq = deque()
        self.dq.append(root)
        ret = dfs()
        return ret

# Main section
for arr_llist, arr_btree in [
                               ([4,2,8], '[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]'),
                               ([1,4,2,6], '[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]'),
                               ([1,4,2,9], '[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]'),
                               ([1,4,2,8,3], '[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]'),
                               ([1,4,2,8,3,7], '[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]'),
                               ([7,1,4,2,8,3], '[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]'),
                            ]:
    print(f'arr_llist, arr_btree = {arr_llist}, {arr_btree}')
    root = deserialize_btree(arr_btree)
    head = deserialize_llist(arr_llist)
    sol = Solution()
    r = sol.isSubPath(head, root)
    print(f'r = {r}')
    print('===========================')

