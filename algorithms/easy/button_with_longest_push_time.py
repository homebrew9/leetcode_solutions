from typing import List
from collections import defaultdict

class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        hsh = defaultdict(int)
        for i, (idx, time) in enumerate(events):
            if i == 0:
                hsh[idx] = time
            else:
                diff = time - events[i-1][1]
                hsh[idx] = max(hsh[idx], diff)
        arr = sorted([(k, v) for k, v in hsh.items()], key=lambda x: (-x[1], x[0]))
        return arr[0][0]

# Main section
for events in [
                 [[1,2],[2,5],[3,9],[1,15]],
                 [[10,5],[1,7]],
                 [[10,5]],
                 [[1,5],[2,7],[3,9],[4,11]],
                 [[1,5],[1,12],[2,17],[2,24]],
              ]:
    print(f'events = {events}')
    sol = Solution()
    r = sol.buttonWithLongestTime(events)
    print(f'r = {r}')
    print('======================')


