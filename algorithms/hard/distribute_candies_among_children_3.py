def cal(x):
    if x < 0:
        return 0
    return x * (x - 1) // 2

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return (
            cal(n + 2)
            - 3 * cal(n - limit + 1)
            + 3 * cal(n - (limit + 1) * 2 + 2)
            - cal(n - 3 * (limit + 1) + 2)
        )

# Main section
for n, limit in [
                   (5, 2),
                   (3, 3),
                   (100000000, 99909911),
                ]:
    print(f'n, limit = {n}, {limit}')
    sol = Solution()
    r = sol.distributeCandies(n, limit)
    print(f'r = {r}')
    print('=============')


