import string

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
    print(f'r = {r}')
    print('============================')

















