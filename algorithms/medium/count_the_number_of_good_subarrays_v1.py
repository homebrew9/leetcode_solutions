from typing import List
from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)
        hsh = defaultdict(int)
        count = 0
        res = 0
        i, j = 0, 0
        while j < N:
            hsh[nums[j]] += 1
            count += hsh[nums[j]] - 1
            while count >= k:
                res += N - j
                hsh[nums[i]] -= 1
                count -= hsh[nums[i]]
                if hsh[nums[i]] == 0:
                    del hsh[nums[i]]
                i += 1
            j += 1
        return res

# Main section
for nums, k in [
                  ([1,1,1,1,1], 10),
                  ([3,1,4,3,2,2,4], 2),
                  ([1,1,1,1,1,1], 10),
                  ([3,3,2,2,4,4], 2),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.countGood(nums, k)
    print(f'r = {r}')
    print('=============')

