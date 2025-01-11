from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1]+nums[i], nums[i])
        return max(nums)

# Main section
sol = Solution()
for nums in [
                 [-2, 1, -3, 4, -1, 2, 1, -5, 4],
                 [1, 2, 3, 4, 5],
                 [-1, -2, -3, -4, -5],
                 [5, 4, -1, 7, 8],
                 [1, -1, 1, -1, 1, -1],
                 [1, -1],
                 [1],
                 [1, 2, 3, -1, -2, -3],
                 [1, 1, 1, 1, 1, 1, 1],
            ]:
    print(f'nums = {nums}')
    r = sol.maxSubArray(nums)
    print(f'r = {r}')
    print('==========================')

