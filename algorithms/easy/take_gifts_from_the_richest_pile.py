from typing import List
import heapq, math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h = [-x for x in gifts]
        heapq.heapify(h)
        for _ in range(k):
            n = -heapq.heappop(h)
            heapq.heappush(h, -math.floor(math.sqrt(n)))
        return -sum(h)

# Main section
for gifts, k in [
                   ([25,64,9,4,100], 4),
                   ([1,1,1,1], 4),
                   ([38,73,86,77,21,10,78,83,17,10,33,88,56,14,4,74,32,57,100,10,12,92,73,55,47,91,3,68,29,64,62,19,8,87,34,74,37,72,94,9,57,59,73,90,33,20,16,5,64,85,11,76,93,35,93,23,17,21,48,35], 29),
                ]:
    print(f'gifts, k = {gifts}, {k}')
    sol = Solution()
    r = sol.pickGifts(gifts, k)
    print(f'r = {r}')
    print('=================')

