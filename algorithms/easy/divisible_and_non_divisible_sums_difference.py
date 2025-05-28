class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res = 0
        for i in range(1, n+1):
            if i % m != 0:
                res += i
            else:
                res -= i
        return res

# Main section
for n, m in [
               (10, 3),
               (5, 6),
               (5, 1),
               (997, 13),
               (1000, 1),
            ]:
    print(f'n, m = {n}, {m}')
    sol = Solution()
    r = sol.differenceOfSums(n, m)
    print(f'r  = {r}')
    print('============================')















