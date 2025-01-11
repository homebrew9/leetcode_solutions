class Solution:
    #def checkString(self, s: str) -> bool:
    #    ind = s.find('b')
    #    if s.find('a', ind+1) > 0:
    #        return False
    #    return True

    def checkString(self, s: str) -> bool:
        return False if s.find('a', s.find('b') + 1) > 0 else True

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


