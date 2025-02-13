from typing import List
import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            val = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, val)
            res += 1
        return res

# Main section
for nums, k in [
                  ([2,11,10,1,3], 10),
                  ([1,1,2,4,9], 20),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.minOperations(nums, k)
    print(f'r = {r}')
    print('=========================')

