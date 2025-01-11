class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # DP with memoization
        def f(t, n):
            if (t, n) in self.memo:
                return self.memo[(t, n)]
            if t < n:
                self.memo[(t, n)] = 0
                return self.memo[(t, n)]
            if n == 1:
                if 1 <= t <= k:
                    self.memo[(t, n)] = 1
                else:
                    self.memo[(t, n)] = 0
                return self.memo[(t, n)]
            res = 0
            for x in range(1, k+1):
                res += f(t - x, n-1)
            self.memo[(t, n)] = res % MOD
            return self.memo[(t, n)]
        MOD = 10**9 + 7
        self.memo = dict()
        return f(target, n)

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
                    ]:
    print(f'n, k, target = {n}, {k}, {target}')
    sol = Solution()
    r = sol.numRollsToTarget(n, k, target)
    print(f'r = {r}')
    print('=================')

