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

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def print_list(head):
            res = list()
            while head:
                res.append(head.val)
                head = head.next
            return res
        def get_half(head):
            # Find out the node count. Then iterate again and split.
            cnt = 0
            node = head
            while node:
                cnt += 1
                node = node.next
            node = head
            prev = None
            for _ in range(cnt//2):
                prev = node
                node = node.next
            if prev:
                prev.next = None
            left = head
            right = None if not prev else node
            return (left, right)
        def merge_sort(head):
            if head is None or head.next is None:
                return head
            left, right = get_half(head)
            head1 = merge_sort(left)
            head2 = merge_sort(right)
            head_new = merge(head1, head2)
            return head_new
        def merge(head1, head2):
            head = ListNode()
            node = head
            node1 = head1
            node2 = head2
            while node1 and node2:
                if node1.val <= node2.val:
                    node.next = node1
                    node1 = node1.next
                    node = node.next
                else:
                    node.next = node2
                    node2 = node2.next
                    node = node.next
            while node1:
                node.next = node1
                node1 = node1.next
                node = node.next
            while node2:
                node.next = node2
                node2 = node2.next
                node = node.next
            return head.next
        return merge_sort(head)

# Main section
for arr in [
              [4,2,1,3],
              [-1,5,3,4,0],
              [],
              [9],
              [8,0],
              [8,9,-9],
              [9,8,7,6,5,4,3,2,1,0],
           ]:
    print(f'arr = {arr}')
    head = deserialize(arr)
    print(f'head = {head}')
    print(serialize(head))
    sol = Solution()
    r = sol.sortList(head)
    print(f'r = {r}')
    print(serialize(r))
    print('==========================')


