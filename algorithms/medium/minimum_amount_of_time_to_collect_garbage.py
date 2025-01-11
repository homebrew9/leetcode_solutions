from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total = garbage[0].count('G') + garbage[0].count('P') + garbage[0].count('M')
        gi, pi, mi = 0, 0, 0
        for i in range(1, len(garbage)):
            if garbage[i].count('G') > 0:
                while gi < i:
                    total += travel[gi]
                    gi += 1
                total += garbage[i].count('G')
            if garbage[i].count('P') > 0:
                while pi < i:
                    total += travel[pi]
                    pi += 1
                total += garbage[i].count('P')
            if garbage[i].count('M') > 0:
                while mi < i:
                    total += travel[mi]
                    mi += 1
                total += garbage[i].count('M')
        return total


# Main section
for garbage, travel in [
                          (['G','P','GP','GG'], [2,4,3]),
                          (['MMM','PGM','GP'], [3,10]),
                          (['G','G','P'], [7,11]),
                          (['G','G','PP'], [7,11]),
                       ]:
    print(f'garbage, travel = {garbage}, {travel}')
    sol = Solution()
    r = sol.garbageCollection(garbage, travel)
    print(f'r = {r}')
    print('=================')

