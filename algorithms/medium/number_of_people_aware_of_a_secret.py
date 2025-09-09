class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        # dp[i] = number of people who found the secret on day i
        dp = [0] * (n + 1)
        dp[1] = 1 # One person finds secret on day 1

        share = 0 # Number of people who can share the secret
        for i in range(2, n+1):
            # Add people who can start sharing today
            if i - delay > 0:
                share += dp[i - delay]
            # Remove people who forgot today
            if i - forget > 0:
                share -= dp[i - forget]
            # Number of new people on day i is the number of people who can share
            dp[i] = share

        # Sum of people who know the secret on day n
        # These are the people who found it within the last "forget" days
        total_knowers = 0
        for i in range(n - forget + 1, n + 1):
            total_knowers += dp[i]
        res = total_knowers % MOD
        return res

# Main section
for n, delay, forget in [
                           (6, 2, 4),
                           (4, 1, 3),
                           (1000, 11, 31),
                        ]:
    print(f'n, delay, forget = {n}, {delay}, {forget}')
    sol = Solution()
    r = sol.peopleAwareOfSecret(n, delay, forget)
    print(f'r = {r}')
    print('========================')









