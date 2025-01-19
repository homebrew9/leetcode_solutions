from typing import List
from heapq import heapify, heappush, heappop

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # We use a Min Heap to store the min seconds each worker uses to destroy the mountain.
        # Of all these min seconds, we have to pick the max value. For example, if 4 workers
        # individually use [3,2,3,4] min seconds to destroy the mountain, then, working together,
        # they will destroy it in a minimum of 4 seconds.
        # In 1st round, worker0 uses: w[0] seconds.
        # In 2nd round, worker0 uses: w[0]*2 seconds
        # In 3rd round, worker0 uses: w[0]*3 seconds and so on
        h = [(t, t, 1) for t in workerTimes]
        heapify(h)
        res = 0
        print(h)
        while mountainHeight > 0:
            print(f'\tmountainHeight, h = {mountainHeight}, {h}')
            ps, wt, x = heappop(h)
            res = max(res, ps)
            heappush(h, (ps + wt * (x + 1), wt, x + 1))
            mountainHeight -= 1
        return res

# Main section
for mountainHeight, workerTimes in [
                                      (4, [2,1,1]),
                                      #(10, [3,2,2,4]),
                                      #(5, [1]),
                                      #(5, [1,2,3,4]),
                                   ]:
    print(f'mountainHeight, workerTimes = {mountainHeight}, {workerTimes}')
    sol = Solution()
    r = sol.minNumberOfSeconds(mountainHeight, workerTimes)
    print(f'r = {r}')
    print('==================')


