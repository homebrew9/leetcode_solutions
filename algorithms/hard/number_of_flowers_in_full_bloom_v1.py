from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        start_times = sorted([s for s, e in flowers])
        end_times = sorted([e for s, e in flowers])
        res = list()
        for p in people:
            started_blooming = bisect_right(start_times, p)
            stopped_blooming = bisect_left(end_times, p)
            res.append(started_blooming - stopped_blooming)
        return res

# Main section
for flowers, people in [
                          ([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]),
                          ([[1,10],[3,3]], [3,3,2]),
                       ]:
    print(f'flowers, people = {flowers}, {people}')
    sol = Solution()
    r = sol.fullBloomFlowers(flowers, people)
    print(f'r = {r}')
    print('===============')

