from typing import List
from collections import Counter

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        N = len(nums)
        cntr = Counter(nums)
        arr = [k for k, v in cntr.items() if v == 1]
        # Solve for three cases: k = 1, k = N, 1 < k < N
        if k == 1:
            return max(arr) if len(arr) > 0 else -1
        if k == N:
            return max(nums)
        # At this point, 1 < k < N
        a, b = nums[0], nums[-1]
        if cntr[a] > 1 and cntr[b] > 1:
            return -1
        if cntr[a] == 1 and cntr[b] == 1:
            return max(a, b)
        if cntr[a] == 1:
            return a
        if cntr[b] == 1:
            return b

# Main section
for nums, k in [
                  ([3,9,2,1,7], 3),
                  ([3,9,7,2,1,7], 4),
                  ([0,0], 1),
                  ([0,0], 2),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.largestInteger(nums, k)
    print(f'r = {r}')
    print('================================')

