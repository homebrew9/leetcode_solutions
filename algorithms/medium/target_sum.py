#
# This code works in local environment, but throws TLE in the website (for last 3 test cases).
# It is not memoized.
#
from typing import List

class Solution:
    #def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #    def dfs(i, expr):
    #        print(f'{i}, {expr}')
    #        if i >= size:
    #            #print('====')
    #            if expr == target:
    #                self.res += 1
    #                #print(f'res = {self.res}')
    #            return
    #        dfs(i+1, expr + nums[i])
    #        dfs(i+1, expr - nums[i])
    #    size = len(nums)
    #    self.res = 0
    #    dfs(0, 0)
    #    return self.res
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, expr):
            #print(f'{i}, {expr}')
            if i >= size:
                #print('====')
                if expr == target:
                    return 1
                    #self.res += 1
                    #print(f'res = {self.res}')
                else:
                    return 0
            pos = dfs(i+1, expr + nums[i])
            neg = dfs(i+1, expr - nums[i])
            return pos + neg
        size = len(nums)
        return dfs(0, 0)


# Main section
for nums, target in [
                       #([1,1,1,1,1], 3),
                       #([1], 1),
                       #([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 1000),
                       #([1,1,2,2,2,4,4], 10),
                       ([1,2,1], 2),
                       #([31,4,45,3,44,49,28,6,22,24,40,25,13,46,17,10,2,38,25,15], 25),
                       #([25,14,16,44,9,22,15,27,23,10,41,25,14,35,28,47,39,26,11,38], 43),
                       #([38,21,23,36,1,36,18,3,37,27,29,29,35,47,16,0,2,42,46,6], 14),
                    ]:
    print(f'nums, target = {nums}, {target}')
    sol = Solution()
    r = sol.findTargetSumWays(nums, target)
    print(f'r = {r}')
    print('=================')


