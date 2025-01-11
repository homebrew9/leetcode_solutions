from typing import List
from heapq import heapify, heappop
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cntr = Counter(nums)
        print(f'\tcntr = {cntr}')
        max_heap = [[-v, k] for k, v in cntr.items()]
        heapify(max_heap)
        res = list()
        for _ in range(k):
            _, num = heappop(max_heap)
            res.append(num)
        return res

# Main section
for nums, k in [
                  ([1,1,1,2,2,3], 2),
                  ([1], 1),
                  ([5,9,7,0,-1,9,7,0,11,-7,9,0,5,-1,3,2,1,0,9,4,5], 3),
                  ([8,7,8,3,8,7,8,2,8,2,7,2,8,3,8,7,3,7,2,3,7,3,1,8,3,1,7,7,1,8], 4),
                  ([1,2], 2),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.topKFrequent(nums, k)
    print(f'r = {r}')
    print('=====================')


