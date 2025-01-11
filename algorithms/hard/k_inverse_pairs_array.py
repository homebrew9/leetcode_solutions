class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        def solve(n, k):
            if k == 0:
                return 1
            if k > ((n - 1) * n) // 2:
                return 0
            if n == 1 and k == 1:
                return 0
            if (n, k) in self.memo:
                return self.memo[(n, k)]
            tmp = 0
            x = max(k - n + 1, 0)
            while x <= k:
                tmp += solve(n - 1, x)
                x += 1
            #for i in range(0, min(k, n-1) + 1):
            #    tmp = (tmp + solve(n - 1, k - i)) % MOD
            self.memo[(n, k)] = tmp % MOD
            return self.memo[(n, k)]
        MOD = 10**9 + 7
        self.memo = dict()
        res = solve(n, k)
        print(self.memo)
        return res

# Main section
for n, k in [
               (10, 7),
               #(900, 250),
               #(1000, 1000),
            ]:
    print(f'n, k = {n}, {k}')
    sol = Solution()
    r = sol.kInversePairs(n, k)
    print(f'r = {r}')
    print('=================')

