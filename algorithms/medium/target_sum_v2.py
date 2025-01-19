# 
# 1) Recursion + Functools cache
# 2) Iterative method - using two dictionaries
#
from typing import List
from functools import cache
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, total):
            if i == N:
                return 1 if total == target else 0
            return dfs(i+1, total + nums[i]) + dfs(i+1, total - nums[i])
        N = len(nums)
        return dfs(0, 0)

    def findTargetSumWays_1(self, nums: List[int], target: int) -> int:
        # Based on lee215's solution
        total_ways = defaultdict(int)
        total_ways[0] = 1
        for n in nums:
            ways_till_now = defaultdict(int)
            for w in total_ways:
                ways_till_now[w + n] += total_ways[w]
                ways_till_now[w - n] += total_ways[w]
            total_ways = ways_till_now
        return total_ways[target]

# Main section
for nums, target in [
                       ([1,1,1,1,1], 3),
                       ([1], 1),
                       ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 1000),
                       ([1,1,2,2,2,4,4], 10),
                       ([1,2,1], 2),
                       ([31,4,45,3,44,49,28,6,22,24,40,25,13,46,17,10,2,38,25,15], 25),
                       ([25,14,16,44,9,22,15,27,23,10,41,25,14,35,28,47,39,26,11,38], 43),
                       ([38,21,23,36,1,36,18,3,37,27,29,29,35,47,16,0,2,42,46,6], 14),
                       ([6,20,22,38,11,15,22,30,0,17,34,29,7,42,46,49,30,7,14,5], 28),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.findTargetSumWays(nums, target)
    print(f'r  = {r}')
    r1 = sol.findTargetSumWays_1(nums, target)
    print(f'r1 = {r1}')
    print('=================')


