class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = numRows
        if n == 1 or len(s) <= n:
            return s
        if n == 2:
            return s[0::2] + s[1::2]
        N = len(s)
        chunkLength = 2*n - 2
        arr = list()
        res = ''
        start, end = None, None
        for i in range(0, N):
            if i % chunkLength == 0:
                res += s[i]
            elif i % chunkLength == 1:
                start = i
            elif i % chunkLength == chunkLength - 1:
                end = i
                arr.append([start, end])
        if end is None or end < start:
            end = start + (chunkLength - 2)
            arr.append([start, end])
        #print(arr)
        while True:
            for i in range(0, len(arr)):
                #print(f'\tBegin: arr = {arr}')
                a, b = arr[i]
                if a > b:
                    return res
                if a == b:
                    if 0 <= a < N:
                        res += s[a]
                else:
                    if 0 <= a < N:
                        res += s[a]
                    if 0 <= b < N:
                        res += s[b]
                arr[i] = [a+1, b-1]
                #print(f'\t\tEnd  : arr = {arr}')
        return res

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


