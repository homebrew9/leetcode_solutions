from typing import List

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        min_dist = float('inf')
        N = len(words)

        # Iterating in forward/right direction
        dist = 0
        for i in range(startIndex, startIndex+N):
            #print('\t%2d %2d %s %d'%(i, i%N, words[i%N], dist))
            if words[i%N] == target:
                min_dist = min(min_dist, dist)
            dist += 1
        #print('\t====')

        # Iterating in backward/left direction
        dist = 0
        for i in range(startIndex, startIndex-N, -1):
            #print('\t%2d %2d %s %d'%(i, i%N, words[i%N], dist))
            if words[i%N] == target:
                min_dist = min(min_dist, dist)
            dist += 1
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


