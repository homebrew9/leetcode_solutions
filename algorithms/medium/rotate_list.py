from typing import Optional, List

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

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        node = head
        arr = list()
        while node:
            arr.append(node.val)
            node = node.next
        k = k % len(arr)
        arr = arr[-k:] + arr[:len(arr)-k]
        i = 0
        node = head
        while node:
            node.val = arr[i]
            node = node.next
            i += 1
        return head

# Main section
for arr, k in [
                 ([1,2,3,4,5], 2),
                 ([0,1,2], 4),
                 ([1,2,3,4,5,6,7,8,9,0], 1000005),
                 ([1,2,3,4,5,6,7,8,9,0], 1234567),
              ]:
    print(f'arr, k = {arr}, {k}')
    head = deserialize(arr)
    print(f'head = {head}')
    print(serialize(head))
    sol = Solution()
    r = sol.rotateRight(head, k)
    print(f'r = {r}')
    print(f'rList = {serialize(r)}')
    print('==========================')

