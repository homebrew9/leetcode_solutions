from typing import List
from collections import defaultdict

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        '''  [-2,  -1,  2,  1]
             [-2,  -3, -1,  0]
        '''
        N = len(nums)
        pfx = [None for _ in range(N)]
        for i in range(N):
            pfx[i] = nums[i] if i == 0 else pfx[i-1] + nums[i]
        hsh = defaultdict(list)
        for i, v in enumerate(pfx):
            hsh[v] += [i]
        res = 0
        for i, v in enumerate(pfx):
            if v - k in hsh:
                for j in hsh[v - k]:
                    if j < i:
                        res = max(res, i - j)
            if v == k:
                res = max(res, i + 1)
        return res

# Main section
for nums, k in [
                  ([1,-1,5,-2,3], 3),
                  ([-2,-1,2,1], 1),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.maxSubArrayLen(nums, k)
    print(f'r = {r}')
    print('========================')

