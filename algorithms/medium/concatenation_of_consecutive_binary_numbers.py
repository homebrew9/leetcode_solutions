class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        res = 0
        for i in range(1, n+1):
            k = i.bit_length()
            res = (((res % MOD) * (2**k % MOD)) + (i % MOD)) % MOD
        return res % MOD

# Main section
for n in [
            1,
            3,
            12,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.concatenatedBinary(n)
    print(f'r = {r}')
    print('===========================')





























