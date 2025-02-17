class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)

        # Initialize all dp values to -1 to indicate non-visited states
        dp = [[-1] * 26 for _ in range(N)]

        def dfs(i: int, c: int, dp: list, s: str, k: int) -> int:
            # Memoized value
            if dp[i][c] != -1:
                return dp[i][c]

            # State is not visited yet
            dp[i][c] = 0
            match = c == (ord(s[i]) - ord('a'))
            if match:
                dp[i][c] = 1

            # Non base case handling
            if i > 0:
                dp[i][c] = dfs(i - 1, c, dp, s, k)
                if match:
                    for p in range(26):
                        if abs(c - p) <= k:
                            dp[i][c] = max(dp[i][c], dfs(i - 1, p, dp, s, k) + 1)
            return dp[i][c]

        # Find the maximum dp[N-1][c] and return the result
        res = 0
        for c in range(26):
            res = max(res, dfs(N - 1, c, dp, s, k))
        return res

# Main section
for s, k in [
               ('acfgbd', 2),
               ('abcd', 3),
               ('abcdprtuv', 2),
               ('upqggturvz', 3),
               ('lvedjqaeildalclmevit', 3),
               ('uqjepjcxtnsafxuowmtsyqjwpmfbdnvfvvjjgddwwtqxdeaamu', 3),
               ('wpmfbdjgddwwtqxdeaamu', 3),
            ]:
    print(f's, k = {s}, {k}')
    sol = Solution()
    r = sol.longestIdealString(s, k)
    print(f'r = {r}')
    print('===================')


