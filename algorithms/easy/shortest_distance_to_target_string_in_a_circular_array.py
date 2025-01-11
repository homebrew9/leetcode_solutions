from typing import List

class Solution:
    #def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
    #    if target not in words:
    #        return -1
    #    pos1 = list()
    #    pos2 = list()
    #    for i in range(0, len(words)):
    #        if words[i] == target:
    #            pos1.append(i)
    #    for i in range(len(words)-1, -1, -1):
    #        if words[i] == target:
    #            pos2.append(i - len(words))
    #    print(f'\tpos1, pos2 = {pos1}, {pos2}')
    #    min_val = float('inf')
    #    for n in pos1:
    #        min_val = min(min_val, abs(n - startIndex))
    #    for n in pos2:
    #        min_val = min(min_val, abs(n - startIndex))
    #    return min_val

    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        ind = len(words) + startIndex
        arr = words + words + words
        min_val = float('inf')
        for i, v in enumerate(arr):
            if v == target:
                dist = abs(i - ind)
                min_val = min(min_val, dist)
        return min_val

# Main section
for words, target, startIndex in [
                #(['hello','i','am','leetcode','hello'], 'hello', 1),
                #(['a','b','leetcode'], 'leetcode', 0),
                #(['i','eat','leetcode'], 'ate', 0),
                #(['hello','i','hello','leetcode','hello','abc'], 'hello', 1),
                #(['hello','i','hello','leetcode','hello','abc'], 'hello', 3),
                #(['hello','i','hello','leetcode','hello','abc'], 'hello', 5),
                #(['hello','i','am','leetcode','okay','abc'], 'hello', 5),
                #(['hello','i','am','leetcode','okay','abc'], 'i', 5),
                #(['hello','i','am','leetcode','okay','abc'], 'am', 5),
                #(['hello','i','am','leetcode','okay','abc'], 'leetcode', 5),
                #(['hello','i','am','leetcode','okay','abc'], 'okay', 5),
                #(['hello','i','am','leetcode','okay','abc'], 'abc', 5),
                (['hsdqinnoha','mqhskgeqzr','zemkwvqrww','zemkwvqrww','daljcrktje','fghofclnwp','djwdworyka','cxfpybanhd','fghofclnwp','fghofclnwp'], 'zemkwvqrww', 8),
             ]:
    print(f'words, target, startIndex = {words}, {target}, {startIndex}')
    sol = Solution()
    r = sol.closetTarget(words, target, startIndex)
    print(f'r = {r}')
    print('================')

