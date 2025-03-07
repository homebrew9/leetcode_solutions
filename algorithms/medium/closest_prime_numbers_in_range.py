from typing import List

class Solution:
    #def closestPrimes(self, left: int, right: int) -> List[int]:
    #    def primes_sieve2(limit):
    #        a = [True] * limit
    #        a[0] = a[1] = False
    #        for (i, isprime) in enumerate(a):
    #            if isprime:
    #                yield i
    #                for n in range(i*i, limit, i):
    #                    a[n] = False

    def closestPrimes(self, left: int, right: int) -> List[int]:
        def primes_sieve2(limit):
            a = [True] * (limit+1)
            a[0] = a[1] = False
            for (i, isprime) in enumerate(a):
                if isprime:
                    yield i
                    for n in range(i*i, limit+1, i):
                        a[n] = False

        arr = list()
        #for p in primes_sieve2(right+1):
        for p in primes_sieve2(right):
            if left <= p <= right:
                arr.append(p)
        #print(f'\tarr = {arr}')
        if len(arr) < 2:
            return [-1, -1]
        min_val = float('inf')
        res = list()
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] < min_val:
                min_val = arr[i] - arr[i-1]
                res = [arr[i-1], arr[i]]
        return res

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

