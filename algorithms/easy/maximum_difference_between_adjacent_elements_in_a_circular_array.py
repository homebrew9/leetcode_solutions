from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max([abs(nums[i % len(nums)] - nums[i-1]) for i in range(1, len(nums) + 1)])

# Main section
for nums in [
               [1,2,4],
               [-5,-10,-5],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maxAdjacentDistance(nums)
    print(f'r  = {r}')
    print('===================')












