from typing import List, Optional

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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def rev(node, diff):
            if diff == 0:
                if not self.leftNode:
                    self.newHead = node
                else:
                    self.leftNode.next = node
                self.rightNode = node.next
                return node
            tmp = rev(node.next, diff-1)
            tmp.next = node
            return node

        #if left == right or not head.next:
        #    return head
        node = head
        self.leftNode, self.rightNode = None, None
        self.newHead = head
        cnt = 0
        diff = right - left
        while node:
            cnt += 1
            if cnt == left:
                tmp = rev(node, diff)
                tmp.next = self.rightNode
                break
            self.leftNode = node
            node = node.next
        return self.newHead

# Main section
for arr, left, right in [
                           ([1,2,3,4,5,6,7,8,9,10], 4, 7),
                           ([1,2,3,4,5,6,7,8,9,10], 1, 4),
                           ([1,2,3,4,5,6,7,8,9,10], 8, 10),
                           ([1,2,3,4,5,6,7,8,9,10], 5, 6),
                           ([1,2,3,4,5,6,7,8,9,10], 7, 7),
                           ([1], 1, 1),
                           ([1,2], 1, 2),
                           ([1,2,3], 1, 3),
                           ([1,2,3,4], 1, 4),
                           ([1,2,3,4], 2, 3),
                        ]:
    print(f'arr, left, right = {arr}, {left}, {right}')
    head = deserialize(arr)
    print(f'head = {head}')
    print(serialize(head))
    sol = Solution()
    r = sol.reverseBetween(head, left, right)
    print(f'r = {r}')
    print(serialize(r))
    print('==========================')


