class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0.0] * (n + 1)
        dp[0] = 1
        s = 1 if k > 0 else 0
        for i in range(1, n + 1):
            dp[i] = s / maxPts
            if i < k:
                s += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                s -= dp[i - maxPts]
        return sum(dp[k:])

# Main section
for n, k, maxPts in [
                       (10, 1, 10),
                       (6, 1, 10),
                       (21, 17, 10),
                    ]:
    print(f'n, k, maxPts  = {n}, {k}, {maxPts}')
    sol = Solution()
    r = sol.new21Game(n, k, maxPts)
    print(f'r = {r}')
    print('==============================')




