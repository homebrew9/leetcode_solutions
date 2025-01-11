class Solution:
    def checkString(self, s: str) -> bool:
        in_block = False
        for ch in s:
            if in_block:
                if ch == 'a':
                    return False
            elif ch == 'b':
                in_block = True
        return True

# Main section
for s in [
            'aaabbb',
            'abab',
            'bbb',
         ]: 
    print(f's = {s}')
    sol = Solution()
    r = sol.checkString(s)
    print(f'r = {r}')
    print('=========================')

