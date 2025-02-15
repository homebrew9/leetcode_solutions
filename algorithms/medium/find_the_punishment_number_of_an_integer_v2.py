class Solution:
    def punishmentNumber(self, n: int) -> int:
        def solve(n):
            if n < 10:
                return {n}
            res = {n}
            i = 10
            while n // i > 0:
                q, r = divmod(n, i)
                tmp = solve(r)
                for x in tmp:
                    res.add(q + x)
                i *= 10
            return res
        ans = 0
        for k in range(1, n + 1):
            nums = solve(k * k)
            if k in nums:
                ans += k * k
        return ans

# Main section
for n in [
            7,
            10,
            37,
            123,
            679,
            1000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.punishmentNumber(n)
    print(f'r = {r}')
    print('=========================')
