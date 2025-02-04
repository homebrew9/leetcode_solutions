# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        first, second = dummy, dummy
        for _ in range(n):
            first = first.next
        while first.next is not None:
            first = first.next
            second = second.next
        # At this point, first has reached the end and second is to the left
        # of the node we have to remove
        second.next = second.next.next
        return dummy.next

# Main section
[1,2,3,4,5]
2
[1]
1
[1,2]
1
