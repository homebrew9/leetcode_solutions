class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        cnt = 0
        for word in text.split():
            st = set(word)
            canType = True
            for ch in st:
                if ch in brokenLetters:
                    canType = False
                    break
            if canType:
                cnt += 1
        return cnt

# Main section
for text, brokenLetters in [
                              ('hello world', 'ad'),
                              ('leet code', 'lt'),
                              ('leet code', 'e'),
                           ]:
    print(f'text, brokenLetters = {text}, {brokenLetters}')
    sol = Solution()
    r = sol.canBeTypedWords(text, brokenLetters)
    print(f'r = {r}')
    print('===================')










