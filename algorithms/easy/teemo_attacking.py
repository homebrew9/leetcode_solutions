#
# Logic doesn't work for ([1,2,3,5,6,7], 10). It returns 15, but correct
# answer is 16.
#
from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0:
            return 0
        size = len(timeSeries)
        total = 0
        for i, v in enumerate(timeSeries):
            #print(f'\t>>> (i, v, total) = ({i}, {v}, {total})')
            total += 1
            #print(f'\t\t>>> (total) = ({total})')
            if i >= size - 1 or timeSeries[i+1] - timeSeries[i] >= duration:
                total += duration - 1
        return total

# Main section
sol = Solution()
for timeSeries, duration in [
                               ([1,4], 2),
                               ([1,2], 2),
                               ([1,2,3,5,6,7], 2),
                               ([1,2,3,5,6,7], 10),
                               ([1,11,21,31,41], 3),
                               ([1,11,21,31,41], 0),
                               ([1], 1),
                               ([1], 9),
                            ]:
    print(f'timeSeries = {timeSeries} ; duration = {duration}')
    r = sol.findPoisonedDuration(timeSeries, duration)
    print(f'r = {r}')
    print('======================')


