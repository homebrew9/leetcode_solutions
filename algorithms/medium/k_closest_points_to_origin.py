from sortedcontainers import SortedDict
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sd = SortedDict()
        for p in points:
            dist = p[0]*p[0] + p[1]*p[1]
            if dist in sd:
                sd[dist] += [p]
            else:
                sd.update({dist: [p]})
            if len(sd) > k:
                sd.popitem(index=-1)
        print(f'\tsd = {sd}')
        res = list()
        for v in sd.values():
            for p in v:
                res.append(p)
                k -= 1
                if k == 0:
                    return res
        return res

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

