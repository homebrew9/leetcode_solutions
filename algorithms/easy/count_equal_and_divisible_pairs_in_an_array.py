from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # TC = O(N^2), SC = O(1)
        N = len(nums)
        res = 0
        for i in range(N):
            for j in range(i+1, N):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    res += 1
        return res
    def countPairs_1(self, nums: List[int], k: int) -> int:
        # TC = O(N), SC = O(N)
        N = len(nums)
        hsh = defaultdict(list)
        res = 0
        for i, v in enumerate(nums):
            if v in hsh:
                for j in hsh[v]:
                    if (i * j) % k == 0:
                        res += 1
            hsh[v] += [i]
        return res

# Main section
for nums, k in [
                  ([3,1,2,2,2,1,3], 2),
                  ([1,2,3,4], 1),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.countPairs(nums, k)
    r1 = sol.countPairs_1(nums, k)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('=============')

