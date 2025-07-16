import string
import re

class Solution:
    def isValid(self, word: str) -> bool:
        valid_chars = string.digits + string.ascii_letters
        vowels = 'aeiouAEIOU'
        if len(word) < 3:
            return False
        vowel_count, consonant_count = 0, 0
        for ch in word:
            if ch not in valid_chars:
                return False
            if ch in vowels:
                vowel_count += 1
            if ch not in vowels and ch not in string.digits:
                consonant_count += 1
        return vowel_count >= 1 and consonant_count >= 1
    def isValid_1(self, word: str) -> bool:
        valid_chars = string.digits + string.ascii_letters
        vowels = 'aeiouAEIOU'
        if len(word) < 3:
            return False
        if any(ch not in valid_chars for ch in word):
            return False
        if sum(ch in vowels for ch in word) == 0:
            return False
        if sum(ch not in vowels and ch not in string.digits for ch in word) == 0:
            return False
        return True
    def isValid_2(self, word: str) -> bool:
        # Needs fixing!
        return len(word) >= 3 and \
               re.match(r'^[0-9a-zA-Z]+$', word) and \
               re.match(r'^.*[aeiouAEIOU].*$', word) and \
               re.match(r'^.*[^aeiouAEIOU0-9].*$', word)
    def isValid_3(self, word: str) -> bool:
        if len(word) >= 3 and re.match(r'^[0-9a-zA-Z]+$', word) and re.match(r'^.*[aeiouAEIOU].*$', word) and re.match(r'^.*[^aeiouAEIOU0-9].*$', word):
            return True
        return False

# Main section
for word in [
               '234Adas',
               'b3',
               'a3$e',
               'UuE6',
            ]:
    print(f'word = {word}')
    sol = Solution()
    r = sol.isValid(word)
    r1 = sol.isValid_1(word)
    #r2 = sol.isValid_2(word)
    r3 = sol.isValid_3(word)
    print(f'r    = {r}')
    print(f'r1   = {r1}')
    #print(f'r2   = {r2}')
    print(f'r3   = {r3}')
    print('============================')


