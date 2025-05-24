from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, v in enumerate(words) if x in v]

# Main section
for words, x in [
                   (['leet','code'], 'e'),
                   (['abc','bcd','aaaa','cbc'], 'a'),
                   (['abc','bcd','aaaa','cbc'], 'z'),
                ]:
    print(f'words, x = {words}, {x}')
    sol = Solution()
    r = sol.findWordsContaining(words, x)
    print(f'r = {r}')
    print('============================')







