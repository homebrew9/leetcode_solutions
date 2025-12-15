from collections import defaultdict
from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        buildings.sort()
        hsh_x = defaultdict(list)
        hsh_y = defaultdict(list)
        for x, y in buildings:
            hsh_x[x] += [y]
            hsh_y[y] += [x]
        res = 0
        for k, v in hsh_x.items():
            if len(v) > 2:
                for yval in v[1:-1]:
                    if k != hsh_y[yval][0] and k != hsh_y[yval][-1]:
                        res += 1
        return res

    def countCoveredBuildings_1(self, n: int, buildings: List[List[int]]) -> int:
        # Another method. No need to sort.
        hsh_x = dict()
        hsh_y = dict()
        for x, y in buildings:
            if x in hsh_x:
                hsh_x[x] = [min(y, hsh_x[x][0]), max(y, hsh_x[x][1])]
            else:
                hsh_x[x] = [y, y]
            if y in hsh_y:
                hsh_y[y] = [min(x, hsh_y[y][0]), max(x, hsh_y[y][1])]
            else:
                hsh_y[y] = [x, x]
        res = 0
        for x, y in buildings:
            if x in hsh_x and y not in hsh_x[x] and y in hsh_y and x not in hsh_y[y]:
                res += 1
        return res

# Main section
for n, buildings in [
                       (3, [[1,2],[2,2],[3,2],[2,1],[2,3]]),
                       (3, [[1,1],[1,2],[2,1],[2,2]]),
                       (5, [[1,3],[3,2],[3,3],[3,5],[5,3]]),
                    ]:
    print(f'n, buildings = {n}, {buildings}')
    sol = Solution()
    r = sol.countCoveredBuildings(n, buildings)
    r1 = sol.countCoveredBuildings_1(n, buildings)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('===========================')








