from bisect import bisect_right
from collections import defaultdict
from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        N = len(nums)
        hsh = defaultdict(list)
        for i, v in enumerate(nums):
            hsh[v] += [i]
        MOD = 10**9 + 7
        res = 0
        for k in hsh:
            if k == 0:
                size = len(hsh[k])
                for i in range(1, size - 1):
                    tmp = i * (size - i - 1)
                    res += tmp
            elif 2 * k in hsh:
                arr = hsh[2*k]
                for i in hsh[k]:
                    idx = bisect_right(arr, i)
                    res += idx * (len(arr) - idx)
        return res % MOD

# Main section
for nums in [
               [6,3,6],
               [0,1,0,0],
               [8,4,2,8,4],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.specialTriplets(nums)
    print(f'r = {r}')
    print('===========================')





























