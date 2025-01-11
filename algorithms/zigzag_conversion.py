from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        def apply_zigzag(a, s, d, c):
            pos = s
            for ch in c:
                a[pos].append(ch)
                pos += direction

        if numRows == 1 or len(s) <= numRows:
            return s
        arr = list()
        retval = ''
        for i in range(numRows):
            arr.append([])

        start = 0
        end = numRows
        direction = 1
        begin = 0
        while True:
            chunk = s[start:end]
            if len(chunk) == 0:
                break
            print(f'    chunk = {chunk}')
            apply_zigzag(arr, begin, direction, chunk)

            start = end
            end = start + numRows - 1
            if direction == 1:
                direction = -1
                begin = numRows - 2
            else:
                direction = 1
                begin = 1

        for row in arr:
            if len(row) == 0:
                return retval
            retval += ''.join(row)
        return retval
        

# Main section
sol = Solution()
for s, numRows in [
                      ('A', 1),
                      ('AB', 1),
                      ('AB', 2),
                      ('AB', 3),
                      #('PAYPALISHIRING', 4),
                      #('PAYPALISHIRING', 3),
                      #('PAYPALISHIRING', 2),
                  ]:
    print('s, numRows = %s, %d'%(s, numRows))
    r = sol.convert(s, numRows)
    print('r = %s'%(r))
    print('=====================================')


