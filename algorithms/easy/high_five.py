from typing import List
from collections import defaultdict
import heapq
from itertools import groupby

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hsh = defaultdict(list)
        for id, score in items:
            hsh[id] += [-score]
        res = list()
        for k, v in hsh.items():
            heapq.heapify(v)
            total = 0
            for _ in range(5):
                total += -heapq.heappop(v)
            res.append([k, total//5])
        return sorted(res)
    def highFive_1(self, items: List[List[int]]) -> List[List[int]]:
        hsh = defaultdict(list)
        for id, score in items:
            hsh[id] += [score]
        res = list()
        for k, v in hsh.items():
            avg = sum(sorted(v)[-5:])//5
            res.append([k, avg])
        return sorted(res)
    def highFive_2(self, items: List[List[int]]) -> List[List[int]]:
        return [[p[0][0], sum([n for _, n in p])//5] for p in [list(g)[-5:] for k, g in groupby(sorted(items), key=lambda x: x[0])]]
    

# Main section
for items in [
                [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]],
                [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]],
             ]:
    print(f'items = {items}')
    sol = Solution()
    r = sol.highFive(items)
    r1 = sol.highFive_1(items)
    r2 = sol.highFive_2(items)
    print(f'r     = {r}')
    print(f'r1    = {r1}')
    print(f'r2    = {r2}')
    print('============================')


