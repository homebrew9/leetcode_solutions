class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res = 0
        for i in range(1, n+1):
            if i % m != 0:
                res += i
            else:
                res -= i
        return res
    def differenceOfSums_1(self, n: int, m: int) -> int:
        return sum([-i if i % m == 0 else i for i in range(1, n+1)])

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
    r1 = sol.differenceOfSums_1(n, m)
    print(f'r    = {r}')
    print(f'r1   = {r1}')
    print('============================')











