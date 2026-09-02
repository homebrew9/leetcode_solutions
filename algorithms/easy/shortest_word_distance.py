from typing import List

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ind1, ind2 = -1, -1
        res = 10**20
        for i, v in enumerate(wordsDict):
            if v == word1:
                if ind2 != -1:
                    res = min(res, i - ind2)
                ind1 = i
            elif v == word2:
                if ind1 != -1:
                    res = min(res, i - ind1)
                ind2 = i
        return res

# Main section
for wordsDict, word1, word2 in [
                                  (['practice', 'makes', 'perfect', 'coding', 'makes'], 'coding', 'practice'),
                                  (['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'coding'),
                                  (['a','b','c','d','e'], 'a', 'e'),
                               ]:
    print(f'wordsDict, word1, word2 = {wordsDict}, {word1}, {word2}')
    sol = Solution()
    r = sol.shortestDistance(wordsDict, word1, word2)
    print(f'r = {r}')
    print('===================================')





















