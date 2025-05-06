from typing import List
from collections import defaultdict
import math

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hsh = defaultdict(int)
        for d in dominoes:
            hsh[tuple(sorted(d))] += 1
        res = 0
        for v in hsh.values():
            res += math.comb(v, 2)
        return res

# Main section
for dominoes in [
                   [[1,2],[2,1],[3,4],[5,6]],
                   [[1,2],[1,2],[1,1],[1,2],[2,2]],
                ]:
    print(f'dominoes = {dominoes}')
    sol = Solution()
    r = sol.numEquivDominoPairs(dominoes)
    print(f'r = {r}')
    print('============================')

