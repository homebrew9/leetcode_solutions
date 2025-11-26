class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]
        rev = s[::-1]
        res = 0
        for a, b in zip(s, rev):
            if a != b:
                res += 1
        return res

# Main section
for n in [
            7,
            10,
            12345,
            293928328,
            3599,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.minimumFlips(n)
    print(f'r = {r}')
    print('===========================')




















