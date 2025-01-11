from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Beautiful algorithm by "conchwu" - we travel from right to left, and update
        # set of garbage types only if it is less than 3.
        res = 0
        st = set()
        for i in range(len(travel) - 1, -1, -1):
            if len(st) < 3:
                st.update(list(garbage[i+1]))
            res += len(st) * travel[i] + len(garbage[i+1])
        res += len(garbage[0])
        return res

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


