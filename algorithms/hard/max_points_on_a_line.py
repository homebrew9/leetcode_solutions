import math
from collections import defaultdict
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        result = 2
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(n):
                if j != i:
                    cnt[math.atan2(points[j][1] - points[i][1],
                                   points[j][0] - points[i][0])] += 1
            result = max(result, max(cnt.values()) + 1)
        return result

# Main section
for points in [
                 [[1,1],[2,2],[3,3]],
                 [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]],
              ]:
    print(f'points = {points}')
    sol = Solution()
    r = sol.maxPoints(points)
    print(f'r = {r}')
    print('=================')

