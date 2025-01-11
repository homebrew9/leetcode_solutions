class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        hsh = dict()
        for i in range(26):
            hsh[i+1] = chr(i+65)
        arr = list()
        while columnNumber > 0:
            q = columnNumber // 26
            r = columnNumber % 26
            if r == 0:
                q -= 1
                r = 26
            arr.append(hsh[r])
            columnNumber = q
        return ''.join(arr[::-1])

# Main section
sol = Solution()
for columnNumber in [
                       1,
                       28,
                       696,
                       697,
                       698,
                       699,
                       700,
                       701,
                       702,
                       703,
                       704,
                       705,
                       706,
                       707,
                       3481,
                       2147483647,
                    ]:
    print(f'columnNumber = {columnNumber}')
    r = sol.convertToTitle(columnNumber)
    print(f'r            = {r}')
    print('================================')

        
