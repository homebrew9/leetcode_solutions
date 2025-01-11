from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deserialize(arr, pos=-1):
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

def serialize(head):
    if not head:
        return None
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

def hasCycle(head):
    nodeSet = set()
    while head:
        if head in nodeSet:
            return True
        nodeSet.add(head)
        head = head.next
    return False

def fetchNode(head, val):
    node = head
    while node.val != val:
        node = node.next
    return node

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr_node = node
        next_node = node.next
        while next_node.next:
            curr_node.val = next_node.val
            curr_node = next_node
            next_node = next_node.next
        curr_node.val = next_node.val
        curr_node.next = None

# Main section
for arr, val in [
                   ([4,5,1,9], 5),
                   ([4,5,1,9], 1),
                   ([4,5,1,9], 4),
                   ([1,2,3,4,5,6,7,8,9], 8),
                   ([1,2,3,4,5,6,7,8,9], 1),
                ]:
    print(f'arr, val = {arr}, {val}')
    head = deserialize(arr)
    print(f'head = {head}')
    print(serialize(head))
    node_to_delete = fetchNode(head, val)
    print(f'node_to_delete = {node_to_delete}')
    sol = Solution()
    r = sol.deleteNode(node_to_delete)
    print(f'head = {head}')
    print(f'linked_list(head) = {serialize(head)}')
    print('==========================')

