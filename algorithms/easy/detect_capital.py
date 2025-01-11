class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.lower() == word or word.upper() == word:
            return True
        if word[0] in [chr(i+65) for i in range(26)] and word[1:].lower() == word[1:] and word[1:].upper() != word[1:]:
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

