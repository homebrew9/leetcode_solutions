from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def primes_sieve2(limit):
            a = [True] * (limit+1)
            a[0] = a[1] = False
            for (i, isprime) in enumerate(a):
                if isprime:
                    yield i
                    for n in range(i*i, limit+1, i):
                        a[n] = False

        # An optimization - the min diff between two consecutive primes is 1 or 2.
        # [2, 3] => diff = 1 : these are the only two consecutiv primes. For all
        # higher primes, the min diff is 2 e.g. [3,5], [11,13], [29,31] etc.
        # So if we see diff < 3, we exit early.
        arr = [-1, -1]
        prev, curr = None, None
        min_val = float('inf')
        for p in primes_sieve2(right):
            if left <= p <= right:
                if prev is None:
                    prev = p
                elif curr is None:
                    curr = p
                    dist = curr - prev
                    if dist < min_val:
                        arr = [prev, curr]
                    if dist < 3:
                        break
                    prev = curr
                    curr = None
        return arr

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

