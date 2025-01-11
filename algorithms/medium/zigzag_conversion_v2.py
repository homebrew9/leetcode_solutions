class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        curRow, step = 0, 1
        rows = [''] * numRows
        #print(f'\trows = {rows}')
        for ch in s:
            #print(f'\t\tStart: rows = {rows}')
            rows[curRow] += ch
            if curRow == numRows - 1:
                step = -1
            elif curRow == 0:
                step = 1
            curRow += step
            #print(f'\t\tEnd  : rows = {rows}')
            #print('=====')
        return ''.join(rows)

# Main section
for s, numRows in [
                     ('A', 3),
                     ('AB', 3),
                     ('ABC', 3),
                     ('ABCD', 3),
                     ('ABCDE', 4),
                     ('PAYPALISHIRING', 3),
                     ('PAYPALISHIRINGXY', 3),
                     ('PAYPALISHIRINGXYZ', 3),
                     ('PAYPALISHIRINGXYZW', 3),
                     ('ABCDEFGHIJ', 2),
                     ('ABCDEFGHIJ', 1),
                  ]:
    print(f's, numRows = {s}, {numRows}')
    sol = Solution()
    r = sol.convert(s, numRows)
    print(f'r = {r}')
    print('================')


