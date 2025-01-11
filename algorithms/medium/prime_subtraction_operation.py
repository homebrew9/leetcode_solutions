from typing import List
import math

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def sieve(n):
            arr = [0 for _ in range(n+1)]
            for i in range(2, math.isqrt(n)+1):
                for j in range(2*i, n+1, i):
                    arr[j] = 1
            return [i for i, v in enumerate(arr) if i >= 2 and v == 0]
        #if len(nums) == 1 or nums == sorted(nums):
        #    return True
        #N = len(nums)
        primes = set(sieve(1000))
        primes.add(0)
        elem = 0
        for n in nums:
            #print(f'\tn = {n}')
            elem += 1
            while True:
                #print(f'\tn, elem = {n}, {elem}')
                if n < elem:
                    return False
                if n - elem in primes:
                    break
                elem += 1
        return True

# Main section
for nums in [
               [4,9,6,10],
               [6,8,11,12],
               [5,8,3],
               [2,2],
               [998,2],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.primeSubOperation(nums)
    print(f'r = {r}')
    print('================')


