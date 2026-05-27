class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        seen = set()
        for ch in word:
            if ch not in seen:
                if (ch.islower() and ch.upper() in seen) or (ch.isupper() and ch.lower() in seen):
                    res += 1
            seen.add(ch)
        return res

# Main section
for word in [
               'aaAbcBC',
               'abc',
               'abBCab',
               'abBCabABacBCAa',
            ]:
    print(f'word = {word}')
    sol = Solution()
    r = sol.numberOfSpecialChars(word)
    print(f'r = {r}')
    print('==================================')








