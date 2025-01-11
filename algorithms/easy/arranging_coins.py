import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Solve it as a quadratic equation.
        # 1 + 2 + 3 + ... + n = n*(n+1)/2 = s
        # So, given s, we work backwards: we find two consecutive
        # numbers whose product is 2*s.
        # n*(n+1) = 2s => n^2 + n - 2*s = 0. Solve as quadratic equation.
        return int((-1 + math.sqrt(4*2*n + 1))/2)

# Main section
for n in [
            5,
            8,
            26,
            1,
            3,
            6,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            59
         ]:
    sol = Solution()
    print(f'n = {n}')
    r = sol.arrangeCoins(n)
    print(f'r = {r}')
    print('==========================')

