import math
from typing import List

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def time_taken(speed):
            return sum([math.ceil(d / speed) for d in dist[:-1]] + [dist[-1] / speed])
        max_val = 10**7
        left, right = 1, max_val
        while left <= right:
            mid = (left + right) // 2
            val = time_taken(mid)
            if val <= hour:
                right = mid - 1
            else:
                left = mid + 1
        return -1 if left > max_val else left

# Main section
for dist, hour in [
                     ([1,3,2], 6),
                     ([1,3,2], 2.7),
                     ([1,3,2], 1.9),
                     ([85,15,6,58,19,36,99,59,30,65,94,27,96,21,87,43,19,95,10,36,73,79,80,80,93,14,49,38,62,84], 86.66),
                     ([85,15,6,58,19,36,99,59,30,65,94,27,96,21,87,43,19,95,10,36,73,79,80,80,93,14,49,38,62,84], 82.5),
                     ([1,1,100000], 2.01),
                  ]:
    print(f'dist, hour = {dist}, {hour}')
    sol = Solution()
    r = sol.minSpeedOnTime(dist, hour)
    print(f'r = {r}')
    print('===================')



