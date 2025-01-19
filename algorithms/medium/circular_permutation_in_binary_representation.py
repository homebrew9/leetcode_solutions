from typing import List

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # Gray codes are a sequence of integers where each pair of consecutive integers
        # differ by 1 bit in their binary representation.
        #     https://cp-algorithms.com/algebra/gray-code.html
        #     https://en.wikipedia.org/wiki/Gray_code
        gray = [i ^ (i >> 1) for i in range(2**n)]
        ind = gray.index(start)
        return gray[ind:] + gray[:ind]
    def circularPermutation_1(self, n: int, start: int) -> List[int]:
        # How to generate Gray codes using recursion?
        # 1) Level 1: Start with ['0', '1']
        # 2) Level 2: Prefix all elements with 0. Prefix all reversed elements with 1. Append.
        # 3) Repeat 2) for each subsequent level.
        # Note that at level i, len(arr) = 2^i, where i >= 1
        #
        def gray(i):
            if i == 1:
                return ['0', '1']
            arr = gray(i - 1)
            return ['0'+x for x in arr] + ['1'+x for x in arr[::-1]]
        res = gray(n)
        res = [int(x, 2) for x in res]
        ind = res.index(start)
        return res[ind:] + res[:ind]

# Main section
for n, start in [
                   (2, 3),
                   (3, 2),
                   (5, 11),
                   #(9, 35),
                   #(10, 399),
                ]:
    print(f'n, start = {n}, {start}')
    sol = Solution()
    r = sol.circularPermutation(n, start)
    print(f'r  = {r}')
    r1 = sol.circularPermutation_1(n, start)
    print(f'r1 = {r1}')
    print('=====================')


