from heapq import heappush, heappop
from typing import List
from math import ceil

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        hp = []
        for i in nums:
            # Python implements a min-heap, so we negate the value
            # to make it work as a max-heap. This works for both
            # positive and negative integers.
            heappush(hp, -i)
        score = 0
        while k > 0:
            n = -heappop(hp)
            score += n
            heappush(hp, -ceil(n/3))
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


