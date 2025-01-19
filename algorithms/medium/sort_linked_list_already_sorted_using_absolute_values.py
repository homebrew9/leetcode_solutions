# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        neg_head, neg_tail = None, None
        zpos_head = None
        prev, node = None, head
        while node:
            if node.val < 0:
                next_node = node.next
                if prev:
                    prev.next = next_node
                if neg_tail is None and neg_head is None:
                    neg_tail = node
                    neg_head = node
                    node.next = None
                else:
                    node.next = neg_head
                    neg_head = node
                node = next_node
            else:
                if not zpos_head:
                    zpos_head = node
                prev = node
                node = node.next
        if neg_head:
            neg_tail.next = zpos_head
            new_head = neg_head
        else:
            new_head = zpos_head
        return new_head


class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
            if curr.val > curr.next.val:
                # Move to front
                node = curr.next
                curr.next = node.next
                node.next = head
                head = node
            else:
                curr = curr.next
        return head


