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

def deserialize(arr, pos = -1):
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

#class Solution:
#    def hasCycle(self, head: Optional[ListNode]) -> bool:
#        nodeSet = set()
#        while head:
#            if head in nodeSet:
#                return True
#            nodeSet.add(head)
#            head = head.next
#        return False

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = list()
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        print(f'arr = {arr}')
        stack = list()
        for item in arr:
            while len(stack) > 0 and stack[-1] < item:
                stack.pop()
            stack.append(item)
        print(f'stack = {stack}')
        i = 0
        ptr1 = head
        while ptr1:
            if ptr1.val != stack[i]:
                ptr1 = ptr1.next
            else:
                break
        first_node = ptr1
        for j in range(1, len(stack)):
            node1 = ListNode(stack[j])
            ptr1.next = node1
            ptr1 = ptr1.next
        ptr1.next = None

        #while ptr1:
        #    #print(f'ptr1.val = {ptr1.val}')
        #    if ptr1.val != stack[i]:
        #        ptr2 = ptr1.next
        #        ptr1.next = None
        #        ptr1 = ptr2
        #    else:
        #        ptr1 = ptr1.next
        #        i += 1
        return first_node

# Main section
for arr in [
              [5,2,13,3,8],
              [1,1,1,1],
              [1,2,3,4,5,6,5,4,3,2,1],
              [6,5,4,7],
              [6,5,4,7,8],
              [8,7,6,5,4],
              [4],
              [4,5],
              [4,5,6],
              [6,5],
              [4,4,4,4],
              [4,4,4,3,2,1,1,1],
              [1,1,1,1,5,1,1,1,1,4,1,1,1,1,3],
           ]:
    print(f'arr = {arr}')
    head = deserialize(arr)
    print(f'head = {head}')
    #print(hasCycle(head))
    print(serialize(head))
    sol = Solution()
    r = sol.removeNodes(head)
    print(f'r = {r}')
    print(serialize(r))
    print('==========================')

