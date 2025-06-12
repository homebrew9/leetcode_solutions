from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max([abs(nums[i % len(nums)] - nums[i-1]) for i in range(1, len(nums) + 1)])
    def maxAdjacentDistance_1(self, nums: List[int]) -> int:
        res = float('-inf')
        N = len(nums)
        for i in range(N-1):
            res = max(res, abs(nums[i] - nums[i+1]))
        res = max(res, abs(nums[-1] - nums[0]))
        return res

# Main section
for nums in [
               [1,2,4],
               [-5,-10,-5],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maxAdjacentDistance(nums)
    r1 = sol.maxAdjacentDistance(nums)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('===================')














