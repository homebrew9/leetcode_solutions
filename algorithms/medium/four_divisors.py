from typing import List
from math import isqrt
from functools import cache

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # A number n has exactly 4 divisors if and only if:
        # (1) it is the product of two primes, or
        # (2) it is the cube of a prime
        # These two are the necessary and sufficient conditions.
        @cache
        def is_prime(n):
            limit = isqrt(n) + 1
            for i in range(2, limit):
                if n % i == 0:
                    return False
            return True
        @cache
        def get_divisor_sum(n):
            limit = isqrt(n) + 1
            for i in range(2, limit):
                if n % i == 0:
                    j = n // i
                    is_valid = is_prime(i)
                    if (i != j and is_valid and is_prime(j)) or (is_valid and i*i*i == n):
                        return 1 + i + j + n
                    else:
                        break
            return 0
        res = 0
        for num in nums:
            val = get_divisor_sum(num)
            res += val
        return res

# Main section
for nums in [
               [21,4,7],
               [21,21],
               [1,2,3,4,5],
               [1,2,3,4,5,6,7,8,9,10],
               [98645,91932,95506,98457,95219,92232,97356,94025,91256,96516,92589,98566,99583,90947,98172,98815,98771,97991,98693,97568,90092,97402,96451,90594,95536],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.sumFourDivisors(nums)
    print(f'r = {r}')
    print('========================')




















