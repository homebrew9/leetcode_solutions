class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        res = 0
        place_value = 1
        while n > 0:
            r = n & 1
            res += (1 ^ r) * place_value
            place_value *= 2
            n >>= 1
        return res

# Main section
for n in [
            5,
            7,
            10,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.bitwiseComplement(n)
    print(f'r = {r}')
    print('===============================')











