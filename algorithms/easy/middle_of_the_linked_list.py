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

def deserialize(arr, pos):
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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# Main section
for arr in [
              ([1]),
              ([1,2]),
              ([1,2,3]),
              ([1,2,3,4]),
              ([1,2,3,4,5]),
              ([1,2,3,4,5,6]),
              ([1,2,3,4,5,6,7]),
              ([1,2,3,4,5,6,7,8]),
              ([1,2,3,4,5,6,7,8,9]),
              ([1,2,3,4,5,6,7,8,9,10]),
           ]:
    print(f'arr = {arr}')
    head = deserialize(arr, -1)
    print(f'head = {head}')
    #print(hasCycle(head))
    print(serialize(head))
    sol = Solution()
    r = sol.middleNode(head)
    print(f'r     = {r}')
    print(f'r.val = {r.val}')
    print('==========================')

