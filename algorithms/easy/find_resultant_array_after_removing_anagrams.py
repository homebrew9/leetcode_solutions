from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        N = len(words)
        res = list()
        res.append(words[0])
        prev = sorted(words[0])
        for i in range(1, N):
            curr = sorted(words[i])
            if curr != prev:
                res.append(words[i])
                prev = curr
        return res

# Main section
for words in [
                ['abba','baba','bbaa','cd','cd'],
                ['a','b','c','d','e'],
             ]:
    print(f'words = {words}')
    sol = Solution()
    r = sol.removeAnagrams(words)
    print(f'r = {r}')
    print('=====================')

