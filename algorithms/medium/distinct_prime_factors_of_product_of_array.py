import math
from typing import List

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def fetchPrimes(n):
            # Sieve of Eratosthenes
            arr = [1 for _ in range(n+1)]
            lim = math.isqrt(n)
            for i in range(2, lim+1):
                start = 2*i
                while start < len(arr):
                    arr[start] = 0
                    start += i
            #print(f'arr = {arr}')
            res = list()
            for i in range(2, len(arr)):
                if arr[i] == 1:
                    res.append(i)
            return res

        primes = fetchPrimes(1000)
        st = set()
        for n in nums:
            for p in primes:
                if p > n:
                    break
                if n % p == 0:
                    st.add(p)
        #print(st)
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

