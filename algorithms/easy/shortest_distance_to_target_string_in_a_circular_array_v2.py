#
# Single iteration of the array. Since the array is circular, the distance between
# indexes i and j (i < j) could be a) j - i or b) N - j + i, where N = array length.
#
from typing import List

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        min_dist = float('inf')
        N = len(words)
        for i in range(0, N):
            if words[i] == target:
                d1 = abs(i - startIndex)
                d2 = abs(N - d1)
                min_dist = min(min_dist, d1, d2)
        return min_dist

# Main section
for words, target, startIndex in [
                (['hello','i','am','leetcode','hello'], 'hello', 1),
                (['a','b','leetcode'], 'leetcode', 0),
                (['i','eat','leetcode'], 'ate', 0),
                (['hello','i','hello','leetcode','hello','abc'], 'hello', 1),
                (['hello','i','hello','leetcode','hello','abc'], 'hello', 3),
                (['hello','i','hello','leetcode','hello','abc'], 'hello', 5),
                (['hello','i','am','leetcode','okay','abc'], 'hello', 5),
                (['hello','i','am','leetcode','okay','abc'], 'i', 5),
                (['hello','i','am','leetcode','okay','abc'], 'am', 5),
                (['hello','i','am','leetcode','okay','abc'], 'leetcode', 5),
                (['hello','i','am','leetcode','okay','abc'], 'okay', 5),
                (['hello','i','am','leetcode','okay','abc'], 'abc', 5),
                (['hsdqinnoha','mqhskgeqzr','zemkwvqrww','zemkwvqrww','daljcrktje','fghofclnwp','djwdworyka','cxfpybanhd','fghofclnwp','fghofclnwp'], 'zemkwvqrww', 8),
             ]:
    print(f'words, target, startIndex = {words}, {target}, {startIndex}')
    sol = Solution()
    r = sol.closetTarget(words, target, startIndex)
    print(f'r = {r}')
    print('================')



