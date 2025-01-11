import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        coins = 1
        while True:
            n -= coins
            rows += 1
            if n < coins + 1:
                break
            coins += 1
        return rows

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


