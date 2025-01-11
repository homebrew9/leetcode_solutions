class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        if i < 0:
            return word
        return word[:i+1][::-1] + word[i+1:]

# Main section
for word, ch in [
                   ('abcdefd', 'd'),
                   ('xyxzxe', 'z'),
                   ('abcd', 'z'),
                ]:
    print(f'word, ch = {word}, {ch}')
    sol = Solution()
    r = sol.reversePrefix(word, ch)
    print(f'r = {r}')
    print('=================')

