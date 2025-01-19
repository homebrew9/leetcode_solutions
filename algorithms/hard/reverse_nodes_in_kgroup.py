from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, x=0, next=None):
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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Iterative method using stack
        dummy = ListNode()
        curr = dummy
        stack = list()
        num = 0
        node = head
        while node:
            next_node = None
            stack.append(node)
            num += 1
            if num % k == 0:
                next_node = node.next
                while stack:
                    curr.next = stack.pop()
                    curr = curr.next
                curr.next = None
            node = next_node if next_node else node.next
        for n in stack:
            curr.next = n
            curr = curr.next
        curr.next = None
        return dummy.next

# Main section
for arr, k in [
                 ([1,2,3,4,5], 2),
                 ([1,2,3,4,5], 3),
                 ([1,2,3,4,5], 5),
                 ([0], 1),
                 ([1,2], 1),
                 ([1,2], 2),
                 ([1,2,3,4,5,6,7,8,9], 1),
                 ([1,2,3,4,5,6,7,8,9], 2),
                 ([1,2,3,4,5,6,7,8,9], 3),
                 ([1,2,3,4,5,6,7,8,9], 4),
                 ([1,2,3,4,5,6,7,8,9], 5),
                 ([1,2,3,4,5,6,7,8,9], 6),
                 ([1,2,3,4,5,6,7,8,9], 7),
              ]:
    print(f'arr, k = {arr}, {k}')
    head = deserialize(arr)
    print(f'head = {head}')
    print(serialize(head))
    sol = Solution()
    r = sol.reverseKGroup(head, k)
    print(f'r = {r}')
    print(serialize(r))
    print('==========================')






