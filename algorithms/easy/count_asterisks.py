class Solution:
    def countAsterisks(self, s: str) -> int:
        in_block = False
        cnt = 0
        for ch in s:
            if in_block:
                if ch == '|':
                    in_block = False
            elif ch == '|':
                in_block = True
            elif ch == '*':
                cnt += 1
        return cnt

# Main section
for s in [
            'l|*e*et|c**o|*de|',
            'iamprogrammer',
            'yo|uar|e**|b|e***au|tifu|l',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.countAsterisks(s)
    print(f'r = {r}')
    print('==========================')

