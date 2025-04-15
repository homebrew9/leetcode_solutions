class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        # Need to simplify the logic a bit. This works, but looks unnecessarily complicated.
        N = len(word)
        vowels = 'aeiou'
        p = 0
        res = 0
        i, j = 0, 0
        in_block = False
        while j < N:
            if in_block:
                if word[j] == vowels[p]:
                    j += 1
                else:
                    p += 1
                    if p == 5:
                        if len(set(word[i:j])) == 5:
                            res = max(res, j - i)
                        in_block = False
                        p = 0
                        i = j
            elif word[j] == 'a':
                in_block = True
                p = 0
                i = j
            else:
                j += 1
        if len(set(word[i:j])) == 5:
            res = max(res, j - i)
        return res

# Main section
for word in [
               'aeiaaioaaaaeiiiiouuuooaauuaeiu',
               'aeeeiiiioooauuuaeiou',
               'a',
               'uiuuoaoueueuoauoueueauoiiuaoueioueeeaiiaaoaeoeaoaoaueiieueioueeauouuoeiaaioauuaeaaoooiaeuoaaaaeiouei',
            ]:
    print(f'word = {word}')
    sol = Solution()
    r = sol.longestBeautifulSubstring(word)
    print(f'r = {r}')
    print('========================')

