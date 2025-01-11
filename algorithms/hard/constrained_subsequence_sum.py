#
# Incorrect result for the last test case.
#
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        def check(i):
            if i in memo:
                return memo[i]
            if i == N - 1:
                memo[i] = nums[i]
                return memo[i]
            val = nums[i]
            j = i + 1
            res = float('-inf')
            while j < N and j - i <= k:
                res = max(res, check(j))
                j += 1
            memo[i] = max(val, val + res)
            return memo[i]
        N = len(nums)
        memo = dict()
        ret = max(nums[0], check(0))
        print(memo)
        return ret

# Main section
for nums, k in [
                  ([10,2,-10,5,20], 2),
                  ([-1,-2,-3], 1),
                  ([10,-2,-10,-5,20], 2),
                  ([6,3,-9,8,8,-9,9,-6,10,-3,-2,-7,3,-5,5,-9,1,-4,7,5,4,1,-8,8,5,9,5,3,-1,9,9,3,-10,-10,-1,6,9,4,7,-8,-5,-3,3,-5,0,-8,1,-8,6,2], 2),
                  ([6,3,-9,8,8,-9,9,-6,10,-3,-2,-7,3,-5,5,-9,1,-4,7,5,4,1,-8,8,5,9,5,3,-1,9,9,3,-10,-10,-1,6,9,4,7,-8,-5,-3,3,-5,0,-8,1,-8,6,2], 3),
                  ([6,3,-9,8,8,-9,9,-6,10,-3,-2,-7,3,-5,5,-9,1,-4,7,5,4,1,-8,8,5,9,5,3,-1,9,9,3,-10,-10,-1,6,9,4,7,-8,-5,-3,3,-5,0,-8,1,-8,6,2], 1),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.constrainedSubsetSum(nums, k)
    print(f'r = {r}')
    print('===========================')

