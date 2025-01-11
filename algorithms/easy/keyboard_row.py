from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        hsh = dict()
        for i, v in enumerate(['qwertyuiop', 'asdfghjkl', 'zxcvbnm']):
            hsh.update(dict([(c, i) for c in list(v)]))
            hsh.update(dict([(c.upper(), i) for c in list(v)]))
        arr = list()
        is_diff_row = False
        for word in words:
            if len(word) == 1:
                arr.append(word)
                continue
            row = hsh[word[0]]
            for c in range(1, len(word)):
                if hsh[word[c]] != row:
                    is_diff_row = True
                    break
            #print(word, c)
            if not is_diff_row:
                arr.append(word)
            is_diff_row = False
        return arr

# Main section
sol = Solution()
for words in [
                #['Hello','Alaska','Dad','Peace'],
                #['omk'],
                #['adsdf','sfd'],
                #['a'],
                #['aaaaaaaaaa'],
                #['were', 'fads', 'bncm'],
                ['abdfs','cccd','a','qwwewm'],
             ]:
    print(f'words = {words}')
    r = sol.findWords(words)
    print(f'r = {r}')
    print('======================')

