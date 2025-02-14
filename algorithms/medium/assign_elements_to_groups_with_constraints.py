import math
from typing import List
from sortedcontainers import SortedList

class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        hsh = dict()
        for i, e in enumerate(elements):
            if e not in hsh:
                hsh[e] = i
        gsize = len(groups)
        res = [-1 for _ in range(gsize)]
        for i, g in enumerate(groups):
            sl = SortedList()
            for n in range(1, math.isqrt(g) + 1):
                if g % n == 0:
                    if n in hsh:
                        sl.add(hsh[n])
                    if g // n in hsh:
                        sl.add(hsh[g//n])
            if len(sl) > 0:
                res[i] = sl[0]
        return res

# Main section
for groups, elements in [
                           ([8,4,3,2,4], [4,2]),
                           ([2,3,5,7], [5,3,3]),
                           ([10,21,30,41], [2,1]),
                        ]:
    print(f'groups, elements = {groups}, {elements}')
    sol = Solution()
    r = sol.assignElements(groups, elements)
    print(f'r = {r}')
    print('===========================')

