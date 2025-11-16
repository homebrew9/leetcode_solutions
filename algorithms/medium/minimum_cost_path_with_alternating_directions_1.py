class Solution:
    def minCost(self, m: int, n: int) -> int:
        # After trying it out with pen and paper, it is easy to see that the moves
        # cancel each other. Movement is possible only for trivial grids of sizes
        # 1x1, 1x2, and 2x1.
        if m == 1 and n == 1:
            return 1
        if (m == 1 and n == 2) or (m == 2 and n == 1):
            return 3
        return -1

# Main section
for m, n in [
               (1, 1),
               (2, 1),
               (1, 2),
               (1000, 1000),
            ]:
    print(f'm, n = {m}, {n}')
    sol = Solution()
    r = sol.minCost(m, n)
    print(f'r = {r}')
    print('=====================')


