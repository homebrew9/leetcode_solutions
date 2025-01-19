from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = [(v, i) for i, v in enumerate(nums)]
        heapq.heapify(h)
        for _ in range(k):
            val, idx = heapq.heappop(h)
            heapq.heappush(h, (val * multiplier, idx))
        return [v for v, _ in sorted(h, key=lambda x: x[1])]

# Main section
for nums, k, multiplier in [
                              ([2,1,3,5,6], 5, 2),
                              ([1,2], 3, 4),
                           ]:
    print(f'nums, k, multiplier = {nums}, {k}, {multiplier}')
    sol = Solution()
    r = sol.getFinalState(nums, k, multiplier)
    print(f'r = {r}')
    print('======================')


