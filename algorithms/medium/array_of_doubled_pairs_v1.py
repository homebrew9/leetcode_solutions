#
# Very simple solution by LC Solutions!
#
from collections import Counter
from typing import List

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cntr = Counter(arr)
        for x in sorted(arr, key=abs):
            if cntr[x] == 0:
                continue
            if cntr[2*x] == 0:
                return False
            cntr[x] -= 1
            cntr[2*x] -= 1
        return True

# Main section
for arr in [
              [3,1,3,6],
              [2,1,2,6],
              [4,-2,2,-4],
              [101,27,43,14,39,2,-20,10,7,78,-30,-10,-15,1,-40,54,5,-5,86,202],
              [-5,-3],
              [2,1,2,1,1,1,2,2],
              [-10,-5,-4,-2,0,0,0,0,1,2,4,8,16,16,32,32,90,180],
              [-10,-5,-4,-2,0,0,0,0,1,2,4,8,16,16,32,32,90,180],
              [-10,-5,-4,-2,0,0,0,0,1,2,4,8,16,16,32,32,90,180,400,401],
              [1,2,1,-8,8,-4,4,-4,2,-2],
              [0,0,0,0],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.canReorderDoubled(arr)
    print(f'r = {r}')
    print('================')

