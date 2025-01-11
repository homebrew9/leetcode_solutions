import math

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        dp = [(None, None) for i in range(n+1)]
        dp[1] = (1, 0)
        dp[n] = (k, None)
        for i in range(n-1, 1, -1):
            dp[i] = (math.ceil(dp[i+1][0]/2), None)
        #print(dp)
        for i in range(2, n+1):
            prev_k, prev_val = dp[i-1]
            curr_k, curr_val = dp[i]

            if (prev_val == 1 and curr_k == prev_k*2-1) or (prev_val == 0 and curr_k == prev_k*2):
                dp[i] = (curr_k, 1)
            elif (prev_val == 1 and curr_k == prev_k*2) or (prev_val == 0 and curr_k == prev_k*2-1):
                dp[i] = (curr_k, 0)

            #if (dp[i-1][1] == 1 and dp[i][0] == dp[i-1][0]*2 - 1) or (dp[i-1][1] == 0 and dp[i][0] == dp[i-1][0]*2 - 1):
            #    dp[i] = (dp[i][0], 0)
            #elif (dp[i-1][1] == 1 and dp[i][0] == dp[i-1][0]*2) or (dp[i-1][1] == 0 and dp[i][0] == dp[i-1][0]*2):
            #    dp[i] = (dp[i][0], 1)
        #print(dp)
        return dp[n][1]

# Main section
for n, k in [
               (1, 1),
               (2, 1),
               (2, 2),
               (3, 1),
               (3, 2),
               (3, 3),
               (3, 4),
               (5, 9),
               (5, 10),
               (30, 123456),
               (28, 9987),
               (28, 100100),
               (25, 456),
               (20, 8765),
            ]:
    print(f'n, k = {n}, {k}')
    sol = Solution()
    r = sol.kthGrammar(n, k)
    print(f'r = {r}')
    print('===================')


