class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r == m-1 or c == n-1:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r][c+1] + dp[r+1][c]
        return dp[0][0]

# Main section
for m, n in [
               (3, 7),
               (3, 2),
               (17, 11),
               (13, 21),
            ]:
    print(f'm, n = {m}, {n}')
    sol = Solution()
    r = sol.uniquePaths(m, n)
    print(f'r = {r}')
    print('===================================')
















