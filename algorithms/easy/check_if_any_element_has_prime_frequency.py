import math
from collections import Counter
from typing import List

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def sieve(n):
            arr = [1 for _ in range(n+1)]
            for i in range(2, math.isqrt(n) + 1):
                for j in range(2*i, n + 1, i):
                    arr[j] = 0
            return set([i for i in range(2, n+1) if arr[i] == 1])
        N = len(nums)
        primes = sieve(N)
        #print(primes)
        cntr = Counter(nums)
        for v in cntr.values():
            if v in primes:
                return True
        return False

# Main section
for nums in [
               [1,2,3,4,5,4],
               [1,2,3,4,5],
               [2,2,2,4,4],
               [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40],
               [12,9,26,53,62,25,14,45,32,71,98,99,70,0,46,84,25,67,20,52,29,3,18,10,70,72,20,94,41,43,5,71,11,42,28,74,87,84,53,71],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.checkPrimeFrequency(nums)
    print(f'r = {r}')
    print('=======================')




