class Solution:
    def minimumMoves(self, s: str) -> int:
        cnt = 0
        i, j = 0, 0
        arr = list(s)
        size = len(arr)
        while True:
            if j > size - 1:
                break
            if arr[j] == 'X':
                cnt += 1
                offset = min(j + 3, size)
                while j < offset:
                    arr[j] = 'O'
                    j += 1
            else:
                j += 1
        return cnt

# Main section
for s in [
            'XXX',
            'XXOX',
            'OOOO',
            'XOOOOXXXO',
            'XOOOOOOOOOX',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.minimumMoves(s)
    print(f'r = {r}')
    print('================')

