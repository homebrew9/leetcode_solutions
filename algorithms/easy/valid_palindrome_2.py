#
# Misunderstood the problem!!!
# Does not work.
#
from typing import List
from collections import Counter

class Solution:
    def validPalindrome(self, s: str) -> bool:
        cntr = Counter(s)
        print(f'cntr = {cntr}')
        n = 0
        for k, v in cntr.items():
            if v % 2 == 1:
                n += 1
            if n > 2:
                return False
        return True

# Main section
for s in [
            #'a',
            #'aa',
            #'ab',
            #'aaa',
            #'aba',
            #'abca',
            #'abc',
            'ppppppqqrrrrrssss',
            'ppppppqqrrrrrsssss',
            'ppppppqqqrrrrrsssss',
            'tebbem',
         ]:
    print(f's = {s}')
    sol = Solution()
    r = sol.validPalindrome(s)
    print(f'r = {r}')
    print('===========================')

