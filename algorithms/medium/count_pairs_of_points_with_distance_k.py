#
# Brute force method. Throws TLE for very long arrays ~ 50K elements!
#
from typing import List

class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        N = len(coordinates)
        res = 0
        for i in range(0, N-1):
            x1, y1 = coordinates[i]
            for j in range(i+1, N):
                x2, y2 = coordinates[j]
                #print(f'\t(x1,y1) = ({x1},{y1}) ; (x2,y2) = ({x2},{y2})')
                #print(f'\t\t(x1^x2) = {x1^x2}')
                if (x1^x2) > k:
                    continue
                #print(f'\t\t\tx1^x2 = {x1^x2}, y1^y2 = {y1^y2}, Sum = {(x1^x2) + (y1^y2)}')
                if (x1^x2) + (y1^y2) == k:
                    res += 1
                    #print(f'\t\t\t\tres = {res}')
            #print('=====')
        return res

# Main section
for coordinates, k in [
                         ([[1,2],[4,2],[1,3],[5,2]], 5),
                         ([[1,3],[1,3],[1,3],[1,3],[1,3]], 0),
                         ([[27,94],[61,68],[47,0],[100,4],[127,89],[61,103],[26,4],[51,54],[91,26],[98,23],[80,74],[19,93]], 95),
                      ]:
    print(f'coordinates, k = {coordinates}, {k}')
    sol = Solution()
    r = sol.countPairs(coordinates, k)
    print(f'r = {r}')
    print('====================')

