import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # A more compact regex: "[A-Z]*|[A-Z]?[a-z]*"
        if re.match('^([a-z]+|[A-Z]+)$', word):
            return True
        if re.match('^[A-Z][a-z]+$', word):
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
            ]:
    print(f'word = {word}')
    sol = Solution()
    r = sol.detectCapitalUse(word)
    print(f'r = {r}')
    print('===========================')


