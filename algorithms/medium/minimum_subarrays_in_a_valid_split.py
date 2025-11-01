from typing import List
from math import gcd
from functools import cache

class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        # If I use math.inf instead of INF then PyLance in VSCode doesn't like it. :(
        INF = 10**20
        n = len(nums)
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if gcd(nums[i - 1], nums[j - 1]) > 1:
                    dp[i] = min(dp[i], dp[j - 1] + 1)
        return -1 if dp[n] == INF else dp[n]

    def validSubarraySplit_1(self, nums: List[int]) -> int:
        @cache
        def solve(i):
            if i >= N:
                return 0
            if nums[i] == 1:
                return -1
            res = 10**10
            for k in range(i, N):
                if gcd(nums[i], nums[k]) != 1:
                    tmp = solve(k+1)
                    if tmp != -1:
                        res = min(res, 1 + tmp)
            return -1 if res == 10**10 else res
        N = len(nums)
        res = solve(0)
        return res

# Main section
for nums in [
               [2,6,3,4,3],
               [3,5],
               [1,2,1],
               [10,98,71,67,84,48,66,49,75,10,93,43,36,51,87,42,84,1,70,80,27,94,13,29,49,63,48,23,17,51,19],
               [135,155,341,603,364,360,74,760,414,58,252,126,688,441,844,133,959,290,468,40,452],
               [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.validSubarraySplit(nums)
    r1 = sol.validSubarraySplit_1(nums)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('=====================')





