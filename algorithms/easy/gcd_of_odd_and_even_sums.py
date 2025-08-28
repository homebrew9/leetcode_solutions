import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return math.gcd(sum(range(1, 2*n+1, 2)), sum(range(2, 2*n+1, 2)))

    def gcdOfOddEvenSums_1(self, n: int) -> int:
        return n

    def gcdOfOddEvenSums_2(self, n: int) -> int:
        # The trivial solution is to just return n.
        # Make sure the proof for that is clear.
        # This is a longer solution that does not use built-in math.gcd function.
        def gcd_euclid(a, b):
            if b == 0:
                return a
            if a >= b:
                return gcd_euclid(b, a - b)
            return gcd_euclid(a, b - a)
        sum_odd = sum(range(1, 2*n + 1, 2))
        sum_even = sum(range(2, 2*n + 1, 2))
        return gcd_euclid(sum_odd, sum_even)

# Main section
for n in [
            1,
            2,
            4,
            5,
            31,
            83,
            159,
            876,
         ]:
    print(f'n  = {n}')
    sol = Solution()
    r = sol.gcdOfOddEvenSums(n)
    r1 = sol.gcdOfOddEvenSums_1(n)
    r2 = sol.gcdOfOddEvenSums_2(n)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print(f'r2 = {r2}')
    print('===================')





