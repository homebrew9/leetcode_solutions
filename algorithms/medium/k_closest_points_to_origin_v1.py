#
# Using sorting via lambda function.
#
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = sorted(points, key=lambda x:x[0]*x[0] + x[1]*x[1])[:k]
        return arr

# Main section
for points, k in [
                    ([[1,3],[-2,2]], 1),
                    ([[3,3],[5,-1],[-2,4]], 2),
                    ([[1,1],[-1,1],[-1,-1],[7,5],[-9,-7]], 3),
                 ]:
    print(f'points, k = {points}, {k}')
    sol = Solution()
    r = sol.kClosest(points, k)
    print(f'r = {r}')
    print('================')

