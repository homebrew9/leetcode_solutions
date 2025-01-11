#
# Recursion with memoization - this works.
#
from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def check(delta):
            if delta in memo:
                return memo[delta]
            cnt = 0
            for n in nums:
                if n <= delta:
                    cnt += check(delta - n)
            memo[delta] = cnt
            return memo[delta]
        memo = dict()
        memo[0] = 1
        return check(target)

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


