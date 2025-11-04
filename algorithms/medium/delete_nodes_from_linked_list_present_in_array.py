from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        dummy = ListNode()
        dummy.next = head
        prev, curr = dummy, head
        while curr:
            if curr.val in nums_set:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next

# Main section
#  (nums, head) = ([1,2,3], [1,2,3,4,5])
#  (nums, head) = ([1], [1,2,1,2,1,2])
#  (nums, head) = ([5], [1,2,3,4])

