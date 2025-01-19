#
# This is similar to Union Find. Check the UF solution, which might be more intuitive.
# In this solution, we are setting the length of 1-group at the range boundaries.
# The value inside the range might be outdated.
#
from typing import List

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        bits = [0] * (len(arr) + 2)
        res = -1
        for i, v in enumerate(arr):
            left, right = bits[v - 1], bits[v + 1]
            if left == m or right == m:
                res = i
            bits[v - left] = bits[v + right] = left + right + 1
        return res

# Main section
for arr, m in [
                 ([3,5,1,2,4], 1),
                 ([3,1,5,4,2], 2),
                 ([2,1], 2),
                 ([1], 1),
              ]:
    print(f'arr, m = {arr}, {m}')
    sol = Solution()
    r = sol.findLatestStep(arr, m)
    print(f'r = {r}')
    print('======================')


