from collections import defaultdict
from typing import List

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def solve(word_list, i):
            hsh = defaultdict(list)
            for word in word_list:
                if len(word) <= 3:
                    self.res[word] = word
                else:
                    left = word[:i+1]
                    right = word[-1]
                    num = len(word) - len(left) - len(right)
                    if num <= 0:
                        continue
                    if num == 1:
                        hsh[word] += [word]
                    else:
                        hsh[left + str(num) + right] += [word]
            if len(hsh) == 0:
                return
            keys = list(hsh.keys())
            for k in keys:
                v = hsh[k]
                if len(v) == 1:
                    self.res[v[0]] = k
                    del hsh[k]
                else:
                    solve(v, i + 1)
        self.res = defaultdict(str)
        solve(words, 0)
        return [self.res[w] for w in words]

# Main section
for words in [
                ['like','god','internal','me','internet','interval','intension','face','intrusion'],
                ['aa','aaa'],
                ['abcdefg','abccefg','abcckkg'],
             ]:
    print(f'words = {words}')
    sol = Solution()
    r = sol.wordsAbbreviation(words)
    print(f'r     = {r}')
    print('============================')

