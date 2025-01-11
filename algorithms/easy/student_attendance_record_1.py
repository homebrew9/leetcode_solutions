import re
class Solution:
    def checkRecord(self, s: str) -> bool:
        if len(re.findall('A', s)) >= 2 or s.find('LLL') >= 0:
            return False
        return True

# Main section
for s in [
            'PPALLP',
            'PPALLL',
            'PPPAPPPAPPPAPPPLLLPPP',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.checkRecord(s)
    print(f'r = {r}')
    print('==========================')


