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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def rev(node):
            if not node.next:
                self.newHead = node
                return node
            tmp = rev(node.next)
            tmp.next = node
            return node
        
        prevNode = None
        slowNode, fastNode = head, head
        while fastNode:
            prevNode = slowNode
            slowNode = slowNode.next
            fastNode = fastNode.next.next
        # We have now reached the center of the linked list
        # Reverse the list from slowNode till the end
        tmp = rev(slowNode)
        tmp.next = None
        prevNode.next = self.newHead
        # So now the first half of the linked list is in the original
        # order and the second half is in reverse order. Just iterate
        # halfway through the linked list and find the max twin sum.
        res = float('-inf')
        node1 = head
        node2 = self.newHead
        while node2:
            res = max(res, node1.val + node2.val)
            node1 = node1.next
            node2 = node2.next
        return res

# Main section
for arr in [
              [5,4,2,1],
              [4,2,2,3],
              [1,100000],
              [1,2,3,4,5,6,7,7,6,5,4,3,2,1],
              [1,2,3,4,5,6],
              [1,2,3,4,5,6,7,8],
              [1,2,3,4,5,6,7,8,9,10],
           ]:
    print(f'arr = {arr}')
    head = deserialize(arr)
    print(f'head = {head}')
    print(serialize(head))
    sol = Solution()
    r = sol.pairSum(head)
    print(f'r = {r}')
    print('==========================')


