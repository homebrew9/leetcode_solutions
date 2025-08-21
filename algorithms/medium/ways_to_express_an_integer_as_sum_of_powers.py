from collections import defaultdict

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        def solve(n, p):
            if n == 0:
                return 1
            if p**x > n:
                return 0
            # We can traverse on two paths from here:
            #   1) Include p, or
            #   2) Exclude p
            # The total no. of ways will be the sum of both paths.
            # If we go with 1) we remove p*p from n and call this function.
            # If we go with 2) we call this function with the next value of p.
            # We memoize this recursive function call by using functools.cache
            # or a separate dictionary that tracks the input parameters.
            if (n, p) in self.hsh:
                return self.hsh[(n, p)]
            path1 = solve(n - p**x, p + 1)
            path2 = solve(n, p + 1)
            self.hsh[(n, p)] = path1 + path2
            return self.hsh[(n, p)]
        MOD = 10**9 + 7
        self.hsh = defaultdict(int)
        res = solve(n, 1)
        return res % MOD

# Main section
for n, x in [
               (10, 2),
               (4, 1),
               (213, 1),
            ]:
    print(f'n, x  = {n}, {x}')
    sol = Solution()
    r = sol.numberOfWays(n, x)
    print(f'r = {r}')
    print('==============================')


















