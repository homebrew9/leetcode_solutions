from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cntr = Counter(arr)
        for k in sorted(cntr, reverse=True):
            if cntr[k] == k:
                return k
        return -1

# Main section
for arr in [
              [2,2,3,4],
              [1,2,2,3,3,3],
              [2,2,2,3,3],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.findLucky(arr)
    print(f'r  = {r}')
    print('===================')









