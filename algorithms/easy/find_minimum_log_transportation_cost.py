class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n > k:
            return (n - k) * k
        if m > k:
            return (m - k) * k
        return 0

# Main section
for n, m, k in [
                  (6, 5, 5),
                  (4, 4, 6),
               ]:
    print(f'n, m, k = {n}, {m}, {k}')
    sol = Solution()
    r = sol.minCuttingCost(n, m, k)
    print(f'r = {r}')
    print('=======================')



















