from typing import List
from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        hsh = defaultdict(int)
        for word in words:
            hsh[word] += 1
        keys = list(hsh.keys())
        for k in keys:
            if k[0] == k[1]:
                v = hsh[k]
                if v % 2 == 0:
                    res += v * 2
                    del hsh[k]
                else:
                    res += (v - 1) * 2
                    hsh[k] = 1
            else:
                r = k[::-1]
                if r in hsh:
                    min_freq = min(hsh[k], hsh[r])
                    res += min_freq * 2 * 2
                    hsh[k] -= min_freq
                    if hsh[k] == 0:
                        del hsh[k]
                    hsh[r] -= min_freq
                    if hsh[r] == 0:
                        del hsh[r]
        # Check if a center can be set
        for k in hsh:
            if k[0] == k[1]:
                res += 2
                break
        return res

# Main section
for words in [
                ['lc','cl','gg'],
                ['ab','ty','yt','lc','cl','ab'],
                ['cc','ll','xx'],
                ['dd','aa','bb','dd','aa','dd','bb','dd','aa','cc','bb','cc','dd','cc'],
                ['nn','nn','hg','gn','nn','hh','gh','nn','nh','nh'],
             ]:
    print(f'words = {words}')
    sol = Solution()
    r = sol.longestPalindrome(words)
    print(f'r  = {r}')
    print('============================')























