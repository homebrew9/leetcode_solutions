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

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def merge(node1, node2):
            if not node1:
                return node2
            elif not node2:
                return node1
            elif node1.val <= node2.val:
                node1.next = merge(node1.next, node2)
                return node1
            else:
                node2.next = merge(node1, node2.next)
                return node2

        node = merge(list1, list2)
        return node

# Main section
for arr1, arr2 in [
                     ([1,2,3], [5,6,7]),
                     ([1,2,5], [3,4,5,6]),
                     ([1,2,5], [3,4,5,6,7,8,9]),
                     ([1,2,4], [1,3,4]),
                     ([1,2,3], [1,2,3]),
                     ([4,5,6,8], [1,2,3,7]),
                     ([1,1,1], [1,1,1]),
                     ([], []),
                     ([], [0]),
                     ([9,9,10], []),
                     ([1,2,3,7,8,11,13], [4,5,6,9,10,12,14]),
                  ]:
    print(f'arr1, arr2 = {arr1}, {arr2}')
    list1 = deserialize(arr1)
    list2 = deserialize(arr2)
    print(f'll(list1) = {serialize(list1)}')
    print(f'll(list2) = {serialize(list2)}')
    sol = Solution()
    r = sol.mergeTwoLists(list1, list2)
    print(f'r = {r}')
    print(f'll(r) = {serialize(r)}')
    print('==========================')

