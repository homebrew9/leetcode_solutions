class Solution:
    def concatHex36(self, n: int) -> str:
        def get_hex_repr(n, base):
            res = ''
            while n > 0:
                q, r = divmod(n, base)
                res = hsh[r] + res
                n = q
            return res
        hsh = {i: str(i) if i < 10 else chr(i + 55) for i in range(36)}
        return get_hex_repr(n*n, 16) + get_hex_repr(n*n*n, 36)

# Main section
for n in [
            13,
            36,
            1,
            500,
            1000,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.concatHex36(n)
    print(f'r = {r}')
    print('===================')

