from typing import List
from sortedcontainers import SortedList
import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Using heap
        h = list()
        for p in piles:
            heapq.heappush(h, -p)
        for _ in range(k):
            curr = -heapq.heappop(h)
            remove = curr // 2
            heapq.heappush(h, -(curr - remove))
        return -sum(h)

    def minStoneSum1(self, piles: List[int], k: int) -> int:
        # Using SortedList
        sl = SortedList(piles)
        for _ in range(k):
            val = sl.pop()
            new_val = val - val//2
            sl.add(new_val)
        return sum(sl)

# Main section
for piles, k in [
                   ([5,4,9], 2),
                   ([4,3,6,7], 3),
                ]:
    print(f'piles, k = {piles}, {k}')
    sol = Solution()
    r = sol.minStoneSum(piles, k)
    print(f'r = {r}')
    r = sol.minStoneSum1(piles, k)
    print(f'r = {r}')
    print('====================')

