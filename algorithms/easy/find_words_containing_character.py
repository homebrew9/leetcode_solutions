from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, v in enumerate(words) if x in v]
    def findWordsContaining_1(self, words: List[str], x: str) -> List[int]:
        res = list()
        for i, word in enumerate(words):
            if x in word:
                res.append(i)
        return res

# Main section
for words, x in [
                   (['leet','code'], 'e'),
                   (['abc','bcd','aaaa','cbc'], 'a'),
                   (['abc','bcd','aaaa','cbc'], 'z'),
                ]:
    print(f'words, x = {words}, {x}')
    sol = Solution()
    r = sol.findWordsContaining(words, x)
    r1 = sol.findWordsContaining_1(words, x)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('============================')















