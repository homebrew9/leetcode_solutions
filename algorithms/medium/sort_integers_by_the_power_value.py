from collections import defaultdict
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        # Top Down DP with memoization
        def collatz(n):
            if n == 1:
                return 0
            if n in memo:
                return memo[n]
            if n % 2 == 0:
                tmp = 1 + collatz(n //2)
            else:
                tmp = 1 + collatz(3 * n + 1)
            memo[n] = tmp
            return memo[n]
        memo = defaultdict(int)
        res = list()
        for n in range(lo, hi + 1):
            c = collatz(n)
            res.append((c, n))
        res.sort()
        return res[k-1][1]

# Main section
for lo, hi, k in [
                    (12, 15, 2),
                    (7, 11, 4),
                    (1, 1000, 3),
                    (1, 1000, 1000),
                 ]:
    print(f'lo, hi, k = {lo}, {hi}, {k}')
    sol = Solution()
    r = sol.getKth(lo, hi, k)
    print(f'r = {r}')
    print('=================')

