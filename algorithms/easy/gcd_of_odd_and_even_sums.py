import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return math.gcd(sum(range(1, 2*n+1, 2)), sum(range(2, 2*n+1, 2)))

    def gcdOfOddEvenSums_1(self, n: int) -> int:
        return n

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
    r1 = sol.gcdOfOddEvenSums(n)
    print(f'r  = {r}')
    print(f'r1 = {r}')
    print('===================')



