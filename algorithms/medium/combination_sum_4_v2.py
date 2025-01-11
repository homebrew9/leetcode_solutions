#
# vanAmsen solution using DP array.
#
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
                    
        return dp[target]

# Main section
for nums, target in [
                       ([1,2,3], 4),
                       ([9], 3),
                       ([4,2,1], 32),
                       ([1,2,3,4,5], 120),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.combinationSum4(nums, target)
    print(f'r = {r}')
    print('=================')



