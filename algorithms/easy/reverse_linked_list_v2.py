from typing import List, Optional
#import MyLinkedList as mll
# =================================================
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
# =================================================
# Using iteration. Time = O(n), Space = O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node, next_node = None, None
        curr_node = head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            # Traverse one step further
            prev_node = curr_node
            curr_node = next_node
        head = prev_node
        return head

# Main section
for arr in [
              [1,2,3,4,5],
              [1,2],
              [],
              [9],
           ]:
    print(f'arr = {arr}')
    head = deserialize(arr)
    print(f'll(head) = {serialize(head)}')
    sol = Solution()
    r = sol.reverseList(head)
    print(f'r = {r}')
    print(f'll(r) = {serialize(r)}')
    print('==========================')

