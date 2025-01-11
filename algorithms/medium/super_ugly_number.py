#
# Works for smaller values of n. Fails for last test case!
#
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        def factorsExist(candidate, primes):
            #print(f'\tcandidate, primes = {candidate}, {primes}')
            for p in primes:
                #print(f'\t\tcandidate, p = {candidate}, {p}')
                while candidate > 1 and candidate >= p and candidate % p == 0:
                    #print(f'\t\t\tInside while...')
                    candidate //= p
                if candidate == 1:
                    return True
            if candidate > 1:
                return False

        if n == 1:
            return 1
        n -= 1
        candidate = 2
        while True:
            print(f'\tn, candidate = {n}, {candidate}')
            if factorsExist(candidate, primes):
                n -= 1
                if n == 0:
                    return candidate
            candidate += 1

# Main section
for n, primes in [
                    #(12, [2,7,13,19]),
                    #(1, [2,3,5]),
                    #(64, [2,5,7,11,13,17,19]),
                    (100000, [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]),
                 ]:
    print(f'n, primes = {n}, {primes}')
    sol = Solution()
    r = sol.nthSuperUglyNumber(n, primes)
    print(f'r = {r}')
    print('==================')

