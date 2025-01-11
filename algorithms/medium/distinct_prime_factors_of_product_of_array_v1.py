import math
from typing import List

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def primes_sieve2(limit):
            a = [True] * (limit+1)
            a[0] = a[1] = False
            for (i, isprime) in enumerate(a):
                if isprime:
                    yield i
                    for n in range(i*i, limit+1, i):
                        a[n] = False

        # Important note - you cannot rewind a generator over and
        # over again!! It moves forward only once! Hence we convert
        # to a list so we can iterate through it multiple times for
        # each n in nums.
        primes = list(primes_sieve2(1000))
        st = set()
        for n in nums:
            #print(f'\tn = {n}')
            for p in primes:
                #print(f'\t\tp = {p}')
                if p > n:
                    break
                if n % p == 0:
                    st.add(p)
                #print(f'\t\t====')
        #print(f'\tst = {st}')
        return len(st)

# Main section
for nums in [
               [2,4,3,7,10,6],
               [2,4,8,16],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.distinctPrimeFactors(nums)
    print(f'r = {r}')
    print('================')


