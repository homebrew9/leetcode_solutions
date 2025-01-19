#
# This is essentially a stack problem - monotonic stack. I still haven't
# wrapped my head around it. I used a SortedList for now.
#
from typing import List
from sortedcontainers import SortedList

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        def is_valid(nums, marker):
            if nums[0] != marker:
                return False
            for i in range(1, len(nums)):
                if nums[i] != nums[i-1] + 1:
                    return False
            return True
        marker = 0
        res = 0
        sl = SortedList()
        for n in arr:
            sl.add(n)
            if is_valid(sl, marker):
                res += 1
                marker = sl[-1] + 1
                sl = SortedList()
        return res

# Main section
for arr in [
              [4,3,2,1,0],
              [1,0,2,3,4],
              [0,5,3,1,4,6,2,7,9,8],
              [0],
              [0,1],
              [1,0,2],
              [0,2,1,3],
              [0,3,2,1,4],
              [1,4,5,2,0,3],
              [5,0,6,3,1,4,2],
              [6,7,3,2,1,5,4,0],
              [4,7,2,5,6,1,3,8,0],
              [2,7,6,1,0,4,5,8,9,3],
              [0,2,1,3,5,6,4,9,8,7],
              [0,3,2,1,5,6,4,9,8,7],
              [0,1,2,3,4,5,6,7,8,9],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.maxChunksToSorted(arr)
    print(f'r = {r}')
    print('=========================')


