from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slowPtr, fastPtr = nums[0], nums[0]
        while True:
            slowPtr = nums[slowPtr]
            fastPtr = nums[nums[fastPtr]]
            if slowPtr == fastPtr:
                break
        slowPtr = nums[0]
        while slowPtr != fastPtr:
            slowPtr = nums[slowPtr]
            fastPtr = nums[fastPtr]
        return slowPtr

# Main section
for nums in [
            ]:
