import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if re.match('^([A-Z]*|[A-Z]?[a-z]*)$', word):
            return True
        return False

# Main section
for word in [
               'USA',
               'leetcode',
               'Google',
               'FlaG',
               'abcDefgHijkL',
               'HappyBirthday',
               'Happybirthday',
               'happybirthday',
               'HAPPYBIRTHDAY',
               'HAPPYBIRTHDAy',
               'happybirthdaY',
               'Fe',
               'a',
               'X',
               'aX',
            ]:
    print(f'word = {word}')
    sol = Solution()
    r = sol.detectCapitalUse(word)
    print(f'r = {r}')
    print('===========================')



