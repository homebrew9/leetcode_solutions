class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(n)] for _ in range(m)]
        # No. of paths at the end are 0
        dp[m-1][n-1] = 0
        # Update the dp list
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                #print(f'\t(r, c) = ({r}, {c}) ; dp = {dp}')
                if r == m-1 and c == n-1:
                    continue
                if r == m-1:
                    dp[r][c] = 1
                elif c == n-1:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r][c+1] + dp[r+1][c]
                #print(f'\t(r, c) = ({r}, {c}) ; dp = {dp}')
        return dp[0][0]

# Main section
for m, n in [
               (3, 2),
               (3, 7),
               (100, 100),
            ]:
    print(f'm, n = {m}, {n}')
    sol = Solution()
    r = sol.uniquePaths(m, n)
    print(f'r = {r}')
    print('=================')

