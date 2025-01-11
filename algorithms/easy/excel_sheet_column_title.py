class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        hsh = {i : chr(i+64) for i in range(1,27)}
        res = ''
        while columnNumber > 0:
            p, q = divmod(columnNumber, 26)
            if q == 0:
                res = hsh[26] + res
                columnNumber = p - 1
            else:
                res = hsh[q] + res
                columnNumber = p
        return res

# Main section
for columnNumber in [
                       26,
                       1,
                       28,
                       701,
                       1000,
                       2000,
                       123456,
                       999999,
                       10000000,
                       1098351087,
                       702,
                       18278,
                       475254,
                       12356630,
                       12356629,
                       5,
                       1,
                       2147483647,
                    ]:
    print(f'columnNumber = {columnNumber}')
    sol = Solution()
    r = sol.convertToTitle(columnNumber)
    print(f'r = {r}')
    print('======================')


