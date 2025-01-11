from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        return ans

# Main section
for nums, k in [
                  ([10,5,2,6], 100),
                  ([1,2,3], 0),
                  ([2,3,4], 24),
                  ([2,2,2,2], 24),
                  ([2,2,2,31,2,3], 24),
                  ([2,3,4,31,2,3], 24),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.numSubarrayProductLessThanK(nums, k)
    print(f'r = {r}')
    print('=================')

