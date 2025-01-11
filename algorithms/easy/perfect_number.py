from typing import List
import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        sum = 0
        for i in range(1, int(math.sqrt(num))+1):
            if num % i == 0:
                #print(f'\ti = {i}')
                sum += i + (num//i)
        #print(sum)
        if sum == 2*num:
            return True
        else:
            return False

# Main section
for num in [
              28,
              7,
              1,
              2,
              3,
              4,
              5,
              6,
              78,
              33550336,
              99999991,
           ]:
    print(f'num = {num}')
    sol = Solution()
    r = sol.checkPerfectNumber(num)
    print(f'r = {r}')
    print('===========================')

