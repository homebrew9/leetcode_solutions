from collections import Counter
from copy import deepcopy
from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cntr = Counter(t)
        left, right = 0, 0
        while True:
            if sum(cntr.values()) == 0 or right == len(s) - 1:
                break
            if s[right] in cntr:
                cntr[s[right]] -= 1
            right += 1
        curr_len = right - left
        curr_sub = s[left:right]
        print(curr_len)
        print(curr_sub)
        return curr_sub

# Main section
for s, t in [
               ('ADOBECODEBANC', 'ABC'),
               #('a', 'a'),
               #('a', 'aa'),
            ]:
    print(f's, t = {s}, {t}')
    sol = Solution()
    r = sol.minWindow(s, t)
    print(f'r = {r}')
    print('=================')

