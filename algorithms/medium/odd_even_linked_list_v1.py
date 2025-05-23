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
        return head
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = head
        evenPtr, oddPtr, oddHead = None, None, None
        n = 0
        node = head
        while node:
            if n == 0:
                evenPtr = node
            elif n == 1:
                oddPtr = node
                oddHead = node
            elif n % 2 == 0:
                evenPtr.next = node
                evenPtr = node
            elif n % 2 == 1:
                oddPtr.next = node
                oddPtr = node
            node = node.next
            if not node:
                if oddHead:
                    evenPtr.next = oddHead
                    oddPtr.next = None
            n += 1
        return newHead

# Main section
for arr in [
              [1,2,3,4,5],
              [2,1,3,5,6,4,7],
              [3,2,0,-4],
              [1,2],
              [1],
              [1,2,3,4,5,6,7,8,9,0],
              [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5],
              [],
              [1,2,3],
              [1,2,3,4,5,6],
           ]:
    print(f'arr = {arr}')
    head = deserialize(arr)
    print(f'head = {head}')
    print(serialize(head))
    sol = Solution()
    r = sol.oddEvenList(head)
    print(f'r = {r}')
    print(serialize(r))
    print('==========================')



