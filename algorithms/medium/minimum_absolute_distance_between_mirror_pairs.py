from typing import List
from collections import defaultdict

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def rev(n):
            res = 0
            while n > 0:
                q, r = divmod(n, 10)
                res = 10 * res + r
                n = q
            return res
        hsh = defaultdict(int)
        MAX = 10**20
        res = MAX
        for i, v in enumerate(nums):
            if v in hsh:
                res = min(res, i - hsh[v])
            r = rev(v)
            hsh[r] = i
        return -1 if res == MAX else res

# Main section
for nums in [
               [12,21,45,33,54],
               [120,21],
               [21,120],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minMirrorPairDistance(nums)
    print(f'r = {r}')
    print('==================================')



