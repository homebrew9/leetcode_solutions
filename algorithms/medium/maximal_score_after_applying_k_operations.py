from typing import List
import math
from sortedcontainers import SortedList

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        sl = SortedList(nums)
        score = 0
        while k > 0:
            n = sl.pop()
            score += n
            sl.add(math.ceil(n/3))
            k -= 1
        return score

# Main section
for nums, k in [
                  ([10,10,10,10,10], 5),
                  ([1,10,3,3,3], 3),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.maxKelements(nums, k)
    print(f'r = {r}')
    print('=================')

