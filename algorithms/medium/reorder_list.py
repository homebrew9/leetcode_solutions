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

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = list()
        node = head
        while node:
            stack.append(node)
            node = node.next
        p1 = head
        p2 = p1.next
        while True:
            if p1 == stack[-1]:
                p1.next = None
                break
            if p2 == stack[-1]:
                p2.next = None
                break
            node = stack.pop()
            p1.next = node
            node.next = p2
            p1 = p2
            p2 = p2.next

# Main section
for arr in [
              [1],
              [1,2],
              [1,2,3],
              [1,2,3,4],
              [1,2,3,4,5],
              [1,2,3,4,5,6],
              [1,2,3,4,5,6,7],
              [1,2,3,4,5,6,7,8],
              [1,2,3,4,5,6,7,8,9],
              [1,2,3,4,5,6,7,8,9,10],
           ]:
    print(f'arr = {arr}')
    head = deserialize(arr)
    print(f'head = {head}')
    print(serialize(head))
    sol = Solution()
    r = sol.reorderList(head)
    print(f'r = {r}')
    print(serialize(head))
    print('==========================')

