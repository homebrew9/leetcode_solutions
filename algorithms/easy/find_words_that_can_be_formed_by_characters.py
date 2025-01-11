from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        s = ''.join(sorted(list(chars)))
        res = 0
        print(f'\ts = {s}')
        for word in words:
            print(f'\t\tword = {word}')
            t = ''.join(sorted(list(word)))
            i = 0
            pos = 0
            while True:
                if i >= len(t):
                    break
                npos = s.find(t[i], pos)
                if npos == -1:
                    break
                pos = npos + 1
                i += 1
            print(f'\t\ti, len(word) = {i}, {len(word)}')
            if i >= len(t):
                res += len(t)
        return res

# Main section
for words, chars in [
                       (['cat','bt','hat','tree'], 'atach'),
                       (['hello','world','leetcode'], 'welldonehoneyr'),
                    ]:
    print(f'words, chars = {words}, {chars}')
    sol = Solution()
    r = sol.countCharacters(words, chars)
    print(f'r = {r}')
    print('===========================')

