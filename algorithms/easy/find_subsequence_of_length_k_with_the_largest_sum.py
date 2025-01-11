from typing import List
from collections import defaultdict

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        hsh = defaultdict(int)
        for i, v in enumerate(nums):
            hsh[(v, i)] = 1
        arr = sorted(hsh.keys(), reverse=True)[:k]
        arr.sort(key=lambda x: x[1])
        return [x for x, y in arr]

# Main section
for nums, k in [
                  ([2,1,3,3], 2),
                  ([-1,-2,3,4], 3),
                  ([3,4,3,3], 2),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.maxSubsequence(nums, k)
    print(f'r = {r}')
    print('================')

