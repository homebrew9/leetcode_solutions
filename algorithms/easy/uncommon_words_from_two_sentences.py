from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1 + ' ' + s2
        cntr = Counter(s.split())
        arr = []
        for k, v in cntr.items():
            if v == 1:
                arr += [k]
        return arr

# Main section
for s1, s2 in [
                 ('this apple is sweet', 'this apple is sour'),
                 ('apple apple', 'banana'),
                 ('the quick brown fox jumps over the lazy dog', 'abracadabra'),
              ]:
    print(f's1 = {s1} ; s2 = {s2}')
    sol = Solution()
    r = sol.uncommonFromSentences(s1, s2)
    print(f'r = {r}')
    print('==========================')

