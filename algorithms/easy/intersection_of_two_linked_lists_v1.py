# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # We start from each list and iterate through it and the other one just once.
        # If there is an intersection, then it will be found during the double iteration.
        # Otherwise, we have two non-intersecting linked lists.
        node_a, node_b = headA, headB
        switched_a, switched_b = False, False
        while node_a is not None and node_b is not None:
            if node_a == node_b:
                return node_a
            node_a = node_a.next
            if node_a is None:
                if not switched_a:
                    node_a = headB
                    switched_a = True
            node_b = node_b.next
            if node_b is None:
                if not switched_b:
                    node_b = headA
                    switched_b = True
        return None

