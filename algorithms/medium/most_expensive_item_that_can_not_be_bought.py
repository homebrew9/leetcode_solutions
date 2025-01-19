from functools import cache
class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        @cache
        def solve(n):
            if n < 0:
                return False
            if n % primeOne == 0 or n % primeTwo == 0:
                return True
            return solve(n - primeOne - primeTwo) or solve(n - primeOne) or solve(n - primeTwo)

        # All items with prices >= primeOne*primeTwo CAN be bought. So we
        # look for prices below primeOne*primeTwo that cannot be expressed
        # as (m * prime1 + n * prime2) and return the highest among them.
        for n in range(primeOne * primeTwo, 0, -1):
            if not solve(n):
                return n

# Main section
import sys
sys.setrecursionlimit(1_000_000_000_000)

for primeOne, primeTwo in [
                             (2, 5),
                             (5, 7),
                             (101, 103),
                             (269, 79),
                             (1269377, 1299689),
                          ]:
    print(f'primeOne, primeTwo = {primeOne}, {primeTwo}')
    sol = Solution()
    r = sol.mostExpensiveItem(primeOne, primeTwo)
    print(f'r = {r}')
    print('==================')


