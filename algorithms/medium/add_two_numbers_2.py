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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = list()
        stack2 = list()
        node = l1
        while node:
            stack1.append(node.val)
            node = node.next
        node = l2
        while node:
            stack2.append(node.val)
            node = node.next
        #print(f'{stack1}, {stack2}')
        num = stack1.pop() + stack2.pop()
        p, q = divmod(num, 10)
        node = ListNode(q)
        carry_over = p
        #print(f'num, node.val = {num}, {node.val}')
        while stack1 and stack2:
            num = stack1.pop() + stack2.pop() + carry_over
            p, q = divmod(num, 10)
            node1 = ListNode(q)
            node1.next = node
            node = node1
            carry_over = p
            #print(f'\tnum, node.val = {num}, {node.val}')
        if stack1 or stack2:
            while stack1:
                num = stack1.pop() + carry_over
                p, q = divmod(num, 10)
                node1 = ListNode(q)
                node1.next = node
                node = node1
                carry_over = p
            while stack2:
                num = stack2.pop() + carry_over
                p, q = divmod(num, 10)
                node1 = ListNode(q)
                node1.next = node
                node = node1
                carry_over = p
        if carry_over > 0:
            node1 = ListNode(carry_over)
            node1.next = node
            node = node1
        return node

# Main section
for arr1, arr2 in [
                     ([7,2,4,3], [5,6,4]),
                     ([2,4,3], [5,6,4]),
                     ([0], [0]),
                     ([9], [9]),
                     ([9,9,9,9,9,9,9,9], [9]),
                     ([9], [9,9,9,9,9,9,9,9]),
                     ([9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9], [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]),
                     ([1,2,3,4,5,6,7,8,9,0], [9,8,7,6,5,4,3,2,1,0]),
                  ]:
    print(f'arr1, arr2 = {arr1}, {arr2}')
    l1 = deserialize(arr1)
    #print(f'l1 = {l1}')
    print(serialize(l1))
    l2 = deserialize(arr2)
    #print(f'l2 = {l2}')
    print(serialize(l2))
    sol = Solution()
    r = sol.addTwoNumbers(l1, l2)
    #print(f'r = {r}')
    print(f'rList = {serialize(r)}')
    print('==========================')

