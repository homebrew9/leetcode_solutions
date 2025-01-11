from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)
        for n in nums:
            if len(h) == k:
                heapq.heappushpop(h, n)
            else:
                heapq.heappush(h, n)
        return h[0]

# Main section
for nums, k in [
                  ([3,2,1,5,6,4], 2),
                  ([3,2,3,1,2,4,5,5,6], 4),
                  ([-5, 3, 1, 0, 9, -7], 1),
                  ([-5, 3, 1, 0, 9, -7], 3),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.findKthLargest(nums, k)
    print(f'r = {r}')
    print('=====================')


