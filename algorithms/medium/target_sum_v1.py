# 
# Recursive DFS + memoization
#
from typing import List

class Solution:
    #def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #    def dfs(i, total):
    #        #print(f'\ti, total, memo = {i}, {total}, {self.memo}')
    #        if (i, total) in self.memo:
    #            return self.memo[(i, total)]
    #        if i >= size:
    #            if total == target:
    #                return 1
    #            else:
    #                return 0
    #        pos = dfs(i+1, total + nums[i])
    #        neg = dfs(i+1, total - nums[i])
    #        self.memo[(i, total)] = pos + neg
    #        return self.memo[(i, total)]
    #    size = len(nums)
    #    self.memo = dict()
    #    ret = dfs(0, 0)
    #    #print(f'memo = {self.memo}')
    #    return ret
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, total):
            #print(f'\ti, total, memo = {i}, {total}, {self.memo}')
            if (i, total) in self.memo:
                return self.memo[(i, total)]
            if i >= size:
                tmp = 1 if total == target else 0
                self.memo[(i, total)] = tmp
                return self.memo[(i, total)]
            pos = dfs(i+1, total + nums[i])
            neg = dfs(i+1, total - nums[i])
            self.memo[(i, total)] = pos + neg
            return self.memo[(i, total)]
        size = len(nums)
        self.memo = dict()
        ret = dfs(0, 0)
        #print(f'memo = {self.memo}')
        return ret

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
    print(f'r = {r}')
    print('=================')



