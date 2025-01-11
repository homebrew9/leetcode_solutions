from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax, curMin = 0, 0
        maxSum, minSum = nums[0], nums[0]
        total = 0
        for x in nums:
            curMax = max(curMax, 0) + x
            maxSum = max(maxSum, curMax)
            curMin = min(curMin, 0) + x
            minSum = min(minSum, curMin)
            total += x
        if total == minSum:
            return maxSum
        else:
            return max(maxSum, total - minSum)

# Main section
for nums in [
               [1,-2,3,-2],
               [5,-3,5],
               [-3,-2,-3],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maxSubarraySumCircular(nums)
    print(f'r = {r}')
    print('===============')

