from typing import List
from sortedcontainers import SortedList

class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        N = len(bulbs)
        sl = SortedList()
        for i, b in enumerate(bulbs):
            sl.add(b)
            idx = sl.index(b)
            if idx > 0 and b - sl[idx-1] == k + 1:
                return i + 1
            if idx < len(sl) - 1 and sl[idx+1] - b == k + 1:
                return i + 1
        return -1

# Main section
for bulbs, k in [
                   ([1,3,2], 1),
                   ([1,2,3], 1),
                ]:
    print(f'bulbs, k  = {bulbs}, {k}')
    sol = Solution()
    r = sol.kEmptySlots(bulbs, k)
    print(f'r  = {r}')
    print('===================')




