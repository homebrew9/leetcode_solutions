import re

class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        lower = -2**31
        upper = 2**31-1
        if re.match(r'^\s*([+-]?\d+).*$', s):
            m = re.match(r'^\s*([+-]?\d+).*$', s)
            num = int(m.group(1))
        if num > upper:
            return upper
        elif num < lower:
            return lower
        else:
            return num

# Main section
sol = Solution()
for s in [
            '42',
            '    -42',
            '4193 with words',
            '   -4096 and some text',
            '       +99999999999999999999999999 3483993 and some more text',
            '       -99999999999999999999999999 3483993 and some more text',
            '-99999999999999999999999999 3483993 and some more text',
            '-999 3483993 xyz',
            '+999 3483993 xyz',
            '999 3483993 xyz',
            '-999.3483993 xyz',
            'words and 987',
            '--987',
            '++987',
            '- 987',
            '+ 987',
         ]:
    print(f's = {s}')
    r = sol.myAtoi(s)
    print(f'r = {r}')
    print('======================')


