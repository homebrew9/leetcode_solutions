from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        for num in nums:
            new_dp = dp[:]  # Copy current state
            for r in range(3):
                new_r = (r + num) % 3
                new_dp[new_r] = max(new_dp[new_r], dp[r] + num)
            dp = new_dp
        return dp[0]

# Main section
for nums in [
               [3,6,5,1,8],
               [4],
               [1,2,3,4,4],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.maxSumDivThree(nums)
    print(f'r = {r}')
    print('===========================')





