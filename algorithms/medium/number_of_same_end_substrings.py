from typing import List
from copy import deepcopy
from collections import Counter
class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        # If ch occurs n times in a string s, then number of substrings
        # that start and end with ch = n + (n-1) + (n-2) + ... + 2 + 1
        # = n * (n+1) // 2
        arr = list()
        cntr = Counter()
        for ch in s:
            cntr[ch] += 1
            arr.append(deepcopy(cntr))
        res = list()
        for x, y in queries:
            if x == 0:
                ctr = arr[y]
            else:
                ctr = arr[y] - arr[x-1]
            res += [sum([v * (v+1) // 2 for v in ctr.values()])]
        return res

# Main section
for s, queries in [
                     ('abcaab', [[0,0],[1,4],[2,5],[0,5]]),
                     ('abcd', [[0,3]]),
                  ]:
    print(f's, queries = {s}, {queries}')
    sol = Solution()
    r = sol.sameEndSubstringCount(s, queries)
    print(f'r = {r}')
    print('====================')

