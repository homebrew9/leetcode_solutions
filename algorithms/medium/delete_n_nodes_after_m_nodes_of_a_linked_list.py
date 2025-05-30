from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        keep, skip = None, None
        keep = head
        while True:
            reached_end = False
            for _ in range(m-1):
                if keep is None:
                    reached_end = True
                    break
                keep = keep.next
            skip = keep
            for _ in range(n):
                if skip is None:
                    reached_end = True
                    break
                skip = skip.next
            if reached_end or skip is None:
                break
            keep.next = skip.next
            keep = keep.next
        if keep is not None:
            keep.next = None
        return head

# Main section
# ([1,2,3,4,5,6,7,8,9,10,11,12,13], 2, 3)
# ([1,2,3,4,5,6,7,8,9,10,11], 1, 3)








