#
# Solution using a single heap
#
from heapq import heapify, heappush, heappop
from typing import List

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        N = len(costs)
        h = list()
        heapify(h)
        for i in range(N):
            if i < candidates:
                heappush(h, (costs[i], 0))
            elif i >= N - candidates:
                heappush(h, (costs[i], 1))
        left, right = candidates, N - candidates - 1
        res = 0
        for i in range(k):
            cost, section = heappop(h)
            res += cost
            if section == 0:
                if left <= right:
                    heappush(h, (costs[left], 0))
                    left += 1
            elif section == 1:
                if left <= right:
                    heappush(h, (costs[right], 1))
                    right -= 1
        return res

# Main section
for costs,k,candidates in [
                             ([17,12,10,2,7,2,11,20,8], 3, 4),
                             ([1,2,4,1], 3, 3),
                             ([1,2,3], 3, 3),
                             ([9,8,7,6,5,4,3,2,1], 4, 2),
                             ([9,8,7,6,5,4,3,2,1], 7, 2),
                             ([1,2,3,4,5,6,7,8,9], 7, 2),
                             ([1,2,3,4,5,6,7,8,9], 1, 1),
                             ([9,8,7,6,5,4,3,2,1], 1, 1),
                             ([1,2,3,9,9,9,1,2,3], 8, 3),
                             ([57,33,26,76,14,67,24,90,72,37,30], 11, 2),
                          ]:
    print(f'costs, k, candidates = {costs}, {k}, {candidates}')
    sol = Solution()
    r = sol.totalCost(costs, k, candidates)
    print(f'r = {r}')
    print('==================')




