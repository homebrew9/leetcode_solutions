from typing import List
import math

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def min_diff(n):
            res = float('inf')
            lst = list()
            for i in range(1, math.isqrt(n)+1):
                if n % i == 0:
                    j = n // i
                    if j - i < res:
                        res = j - i
                        lst = [i, j]
            return (res, lst)
        r1, t1 = min_diff(num+1)
        r2, t2 = min_diff(num+2)
        if r1 <= r2:
            return t1
        return t2
    def closestDivisors_1(self, num: int) -> List[int]:
        # Why check (num+1)%i before (num+2)%i ? Not sure about the proof, but
        # the reverse order fails for num = 1.
        i = math.isqrt(num+2)
        while i > 0:
            if (num+1) % i == 0:
                return [i, (num+1)//i]
            if (num+2) % i == 0:
                return [i, (num+2)//i]
            i -= 1

# Main section
for num in [
              8,
              123,
              999,
              2,
              1
           ]:
    print(f'num = {num}')
    sol = Solution()
    r = sol.closestDivisors(num)
    print(f'r  = {r}')
    r1 = sol.closestDivisors_1(num)
    print(f'r1 = {r1}')
    print('==================')


