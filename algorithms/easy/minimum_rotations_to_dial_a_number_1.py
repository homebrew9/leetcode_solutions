class Solution:
    def minRotations(self, s: str) -> int:
        res = 0
        pos = 0
        for ch in s:
            next_pos = int(ch)
            res += min(abs(pos - next_pos), 10 - abs(pos - next_pos))
            pos = next_pos
        return res

# Main section
for s in [
            '0192837465',
            '1200210200',
            '5155928499',
            '9785610647',
            '0792045642',
            '2515973135',
            '9561254299',
            '5050505050',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.minRotations(s)
    print(f'r = {r}')
    print('===================================')














