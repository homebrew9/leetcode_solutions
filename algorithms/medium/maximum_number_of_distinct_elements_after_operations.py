from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        last_assigned = float('-inf')
        count = 0
        for x in nums:
            # The smallest value we can assign that is > last_assigned
            candidate = max(last_assigned + 1, x - k)
            # Check if candidate is within allowed range
            if candidate <= x + k:
                count += 1
                last_assigned = candidate
        return count

# Main section
for nums, k in [
                  ([1,2,2,3,3,4], 2),
                  ([4,4,4,4], 1),
                  ([1,1000000000], 1000000000),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.maxDistinctElements(nums, k)
    print(f'r = {r}')
    print('=====================')

