from typing import List
from functools import cache
from math import inf

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i: int):
            if i == len(nums) - 1:
                return 0
            res = -inf
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) <= target:
                    res = max(res, dfs(j) + 1)
            return res
        ans = dfs(0)
        return -1 if ans < 0 else ans # type: ignore

# Main section
for nums, target in [
                       ([1,3,6,4,1,2], 2),
                       ([1,3,6,4,1,2], 3),
                       ([1,3,6,4,1,2], 0),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.maximumJumps(nums, target)
    print(f'r = {r}')
    print('==================================')




