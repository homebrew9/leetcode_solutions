#
# Ye Gao's solution. I am still trying to wrap my head around the function: multinom.
# I believe it returns the count of integers given the digit frequencies!!
#
from collections import Counter
import math

#class Solution:
#    def countGoodIntegers(self, n: int, k: int) -> int:
#        def multinom(vals):
#            # Given the digit frequencies in vals, return the
#            # count of integers that could be formed with the
#            # same length as len(vals) using the digits.
#            # Eg. if vals = [1,2], we can have 3 integers.
#            ans = k = 1
#            for x in vals:
#                for i in range(1, x+1):
#                    ans *= k
#                    ans //= i
#                    k += 1
#            return ans
#
#        if n == 1:
#            return 9//k
#        ans = 0
#        half = n//2
#        valid = set()
#        for x in range(1, pow(10, half)):
#            part = str(x).zfill(half)
#            if not part.endswith('0'):
#                if n & 1:
#                    cands = [part[::-1] + str(mid) + part for mid in range(0, 10)]
#                else:
#                    cands = [part[::-1] + part]
#                for cand in cands:
#                    if int(cand) % k == 0:
#                        key = ''.join(sorted(cand))
#                        valid.add(key)
#        #print(f'valid = {valid}')
#
#        for key in valid:
#            freq = Counter(key)
#            val = multinom(freq.values())
#            if freq['0']:
#                freq['0'] -= 1
#                val -= multinom(freq.values())
#            ans += val
#        return ans

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def combinations(hsh):
            # Total combinations = n! / r! / s! / t! ...
            # where r, s, t are the frequencies of the digits.
            # We also have to handle leading 0s.
            res = (n - hsh['0']) * math.factorial(n - 1)
            '''
                10901 => first position cannot be 0 so (5 - 2)
                Already placed one number on first position, so we can take remaining 4
                so (5 - 2)*4*3*2*1 total permutations
            '''
            for v in hsh.values():
                res //= math.factorial(v)
            return res

        if n == 1:
            return 9//k
        ans = 0
        half = n//2
        valid = set()
        for x in range(1, pow(10, half)):
            part = str(x).zfill(half)
            if not part.endswith('0'):
                if n & 1:
                    cands = [part[::-1] + str(mid) + part for mid in range(0, 10)]
                else:
                    cands = [part[::-1] + part]
                for cand in cands:
                    if int(cand) % k == 0:
                        key = ''.join(sorted(cand))
                        valid.add(key)
        #print(f'valid = {valid}')

        for key in valid:
            freq = Counter(key)
            val = combinations(freq)
            ans += val
        return ans


# Main section
for n, k in [
               (3, 5),
               (1, 4),
               (5, 6),
            ]:
    print(f'n, k = {n}, {k}')
    sol = Solution()
    r = sol.countGoodIntegers(n, k)
    print(f'r = {r}')
    print('================')



