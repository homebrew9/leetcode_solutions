class Solution:
    def rotatedDigits(self, n: int) -> int:
        def is_valid(i):
            n_orig = i
            res = 0
            pv = 1
            while i > 0:
                q, r = divmod(i, 10)
                if r not in hsh:
                    return False
                res = hsh[r] * pv + res
                pv *= 10
                i = q
            return res != n_orig
        hsh = {0:0, 1:1, 8:8, 2:5, 5:2, 6:9, 9:6}
        res = 0
        for i in range(1, n+1):
            val = is_valid(i)
            res += int(val)
        return res

# Main section
for n in [
            10,
            1,
            2,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.rotatedDigits(n)
    print(f'r = {r}')
    print('==============================')





