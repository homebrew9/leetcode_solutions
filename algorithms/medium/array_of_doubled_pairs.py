from collections import Counter
from typing import List

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cntr = Counter(arr)
        arr.sort()
        for n in arr:
            #print(f'\tn = {n}')
            if cntr[n] > 0:
                if n == 0:
                    if cntr[n] % 2 != 0:
                        return False
                    cntr[n] = 0
                    continue
                if n < 0:
                    if n % 2 == 1:
                        return False
                    tmp = n // 2
                else:
                    tmp = n * 2
                if tmp not in cntr or cntr[tmp] == 0:
                    return False
                cntr[n] -= 1
                cntr[tmp] -= 1
            #print(f'\tcntr = {cntr}')
            #print('=====')
        return True

# Main section
# Array lengths are even!
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

