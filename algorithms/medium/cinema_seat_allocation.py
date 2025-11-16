from typing import List
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        hsh = defaultdict(set)
        for r, c in reservedSeats:
            hsh[r].add(c)
        res = 0
        for k, v in hsh.items():
            curr = 0
            if 2 not in v and 3 not in v and 4 not in v and 5 not in v:
                curr += 1
            if 6 not in v and 7 not in v and 8 not in v and 9 not in v:
                curr += 1
            if curr > 0:
                res += curr
                continue
            if 4 not in v and 5 not in v and 6 not in v and 7 not in v:
                res += 1
        res += 2 * (n - len(hsh))
        return res

# Main section
for n, reservedSeats in [
                           (3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]),
                           (2, [[2,1],[1,8],[2,6]]),
                           (4, [[4,3],[1,4],[4,6],[1,7]]),
                        ]:
    print(f'n, reservedSeats = {n}, {reservedSeats}')
    sol = Solution()
    r = sol.maxNumberOfFamilies(n, reservedSeats)
    print(f'r = {r}')
    print('=====================')








