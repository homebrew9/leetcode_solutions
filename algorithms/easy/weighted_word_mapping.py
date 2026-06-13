from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return ''.join([chr(25 - sum([weights[ord(c)-97] for c in word])%26 + 97) for word in words])

# Main section
for words, weights in [
                         (['abcd','def','xyz'], [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]),
                         (['a','b','c'], [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]),
                         (['abcd'], [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]),
                      ]:
    print(f'words, weights = {words}, {weights}')
    sol = Solution()
    r = sol.mapWordWeights(words, weights)
    print(f'r = {r}')
    print('===================================')




