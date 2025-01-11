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
    if head is None:
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

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Start with a new node - "res"
        # Compare current node of both lists and add the node with
        # smaller value to "res".
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        res = ListNode(-1000)
        if list1.val < list2.val:
            res.next = list1
            list1.next = self.mergeTwoLists(list1.next, list2)
        else:
            res.next = list2
            list2.next = self.mergeTwoLists(list1, list2.next)
        return res.next

# Main section
for arr1, arr2 in [
                     ([1,3,5], [2,4,6]),
                     ([2], [1,2,3]),
                     ([1,3,4], [1,2,5,6,7]),
                     ([1,2,3], [7,8,9,10,11]),
                     ([1,3,9,10], [2,3,4,6,8,12]),
                     ([], [1,2,3]),
                     ([1,2], []),
                     ([1,20], [5,90]),
                  ]:
    print(f'arr1, arr2 = {arr1}, {arr2}')
    list1 = deserialize(arr1)
    print(f'list1 = {list1}')
    print(serialize(list1))
    list2 = deserialize(arr2)
    print(f'list2 = {list2}')
    print(serialize(list2))
    sol = Solution()
    r = sol.mergeTwoLists(list1, list2)
    print(f'r = {r}')
    print(serialize(r))
    print('==========================')

