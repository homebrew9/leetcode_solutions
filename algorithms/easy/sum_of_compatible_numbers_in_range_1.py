class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        res = 0
        for x in range(max(1, n-k), n+k+1):
            if (n & x) == 0:
                res += x
        return res

# Main section
for n, k in [
               (2, 3),
               (5, 1),
               (4, 9),
               (17, 83),
            ]:
    print(f'n, k = {n}, {k}')
    sol = Solution()
    r = sol.sumOfGoodIntegers(n, k)
    print(f'r = {r}')
    print('==============================')


