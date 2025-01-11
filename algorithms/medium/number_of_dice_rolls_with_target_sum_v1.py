class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # Dynamic Programming - 2D Tabulation Method
        MOD = 10**9 + 7
        dp = [[0 for _ in range(n + 1)] for _ in range(target + 1)]
        for r in range(1, min(k, target) + 1):
            dp[r][1] = 1
        for c in range(2, n + 1):
            for r in range(c, target + 1):
                curr = 0
                delta = 1
                while r - delta >= 0 and delta <= k:
                    curr += dp[r-delta][c-1]
                    delta += 1
                dp[r][c] = curr
        return dp[target][n] % MOD

# Main section
for n, k, target in [
                       (1, 6, 3),
                       (2, 6, 7),
                       (30, 30, 500),
                       (3, 6, 9),
                       (3, 6, 10),
                       (3, 6, 18),
                       (30, 30, 1000),
                       (30, 30, 700),
                       (4, 6, 9),
                       (2, 6, 3),
                       (2, 6, 30),
                    ]:
    print(f'n, k, target = {n}, {k}, {target}')
    sol = Solution()
    r = sol.numRollsToTarget(n, k, target)
    print(f'r = {r}')
    print('=================')


