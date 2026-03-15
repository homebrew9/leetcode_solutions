class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            if i >= 1000:
                res += 1
        return res
    def countCommas_1(self, n: int) -> int:
        return max(0, n - 999)

# Main section
for n in [
            1002,
            998,
            1,
            10000,
            100000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.countCommas(n)
    r1 = sol.countCommas_1(n)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    assert(r == r1)
    print('===============================')

















