class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if encodedText == '':
            return ''
        N = len(encodedText)
        cols = N // rows
        arr = list()
        for i in range(0, N, cols):
            arr.append(list(encodedText[i:i+cols]))
        res = ''
        for col in range(cols):
            r = 0
            c = col
            while r < rows and c < cols:
                res += arr[r][c]
                r += 1
                c += 1
        res = res.rstrip(' ')
        return res

# Main section
for encodedText, rows in [
                            ('ch   ie   pr', 3),
                            ('iveo    eed   l te   olc', 4),
                            ('coding', 1),
                            ('', 5),
                         ]:
    print(f'encodedText, rows = {encodedText}, {rows}')
    sol = Solution()
    r = sol.decodeCiphertext(encodedText, rows)
    print(f'r = {r}')
    print('==================================')






