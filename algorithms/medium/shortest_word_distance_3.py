from typing import List

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        inds = list()
        res = float('inf')
        for i, v in enumerate(wordsDict):
            if v == word1:
                inds.append((v, i))
                if len(inds) > 1 and inds[-2][0] == word2:
                    res = min(res, i - inds[-2][1])
            elif v == word2:
                inds.append((v, i))
                if len(inds) > 1 and inds[-2][0] == word1:
                    res = min(res, i - inds[-2][1])
        return res

# Main section
for wordsDict, word1, word2 in [
                                  (['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'coding'),
                                  (['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'makes'),
                               ]:
    print(f'wordsDict, word1, word2 = {wordsDict}, {word1}, {word2}')
    sol = Solution()
    r = sol.shortestWordDistance(wordsDict, word1, word2)
    print(f'r = {r}')
    print('============================')






