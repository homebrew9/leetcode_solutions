from typing import List
import math

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
            arr = [1 for _ in range(n+1)]
            for i in range(2, math.isqrt(n)+1):
                for j in range(2*i, n+1, i):
                    arr[j] = 0
            return [i for i, v in enumerate(arr) if i >= 2 and v == 1]
        primes = sieve(right)
        min_diff = float('inf')
        for i in range(len(primes) - 1):
            if primes[i] >= left:
                if primes[i+1] - primes[i] < min_diff:
                    min_diff = primes[i+1] - primes[i]
                    a, b = primes[i], primes[i+1]
                # (2, 3) are the only consecutive primes
                # (101, 103) prime diff cannot be less than 2, unless it is (2, 3)
                if min_diff in (1, 2):
                    break
        if min_diff == float('inf'):
            return [-1, -1]
        return [a, b]

# Main section
for left, right in [
                      (10, 19),
                      (4, 6),
                      (220456, 770899),
                      (19, 31),
                      (1, 1000000),
                   ]:
    print(f'left, right = {left}, {right}')
    sol = Solution()
    r = sol.closestPrimes(left, right)
    print(f'r = {r}')
    print('================')

