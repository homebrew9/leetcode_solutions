#
# The original attempt was based on rod cutting. Does not work.
# 
import functools
from typing import List

#class Solution:
#    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
#        print(f'\td = {d}')
#        if d == 0:
#            return 0
#        minDiff = 10**9
#        for i in range(d):
#            minDiff = min(minDiff, jobDifficulty[i] + self.minDifficulty(jobDifficulty, d-i-1))
#        return minDiff

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d: return -1

        @functools.lru_cache(None)
        def dfs(i, d):
            if d == 1:
                return max(jobDifficulty[i:])
            res, maxd = float('inf'), 0
            for j in range(i, n - d + 1):
                maxd = max(maxd, jobDifficulty[j])
                res = min(res, maxd + dfs(j + 1, d - 1))
            return res
        return dfs(0, d)

# Main section
for jobDifficulty, d in [
                           ([6,5,4,3,2,1], 2),
                           ([6,5,4,3,2,1], 3),
                        ]:
    print(f'jobDifficulty, d = {jobDifficulty}, {d}')
    sol = Solution()
    r = sol.minDifficulty(jobDifficulty, d)
    print(f'r = {r}')
    print('=================')

