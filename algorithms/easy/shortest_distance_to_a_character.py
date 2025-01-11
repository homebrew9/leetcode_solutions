from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        pos = []
        pos += [float('-inf')]
        for i, v in enumerate(s):
            if v == c:
                pos += [i]
        pos += [float('inf')]
        
        mark1 = pos[0]
        j = 1
        mark2 = pos[j]
        arr = []
        for i in range(len(s)):
            if i == mark2:
                mark1 = mark2
                j += 1
                mark2 = pos[j]
            arr += [min(abs(i - mark1), abs(i - mark2))]
        return arr

# Main section
for s, c in [
               ('loveleetcode', 'e'),
               ('aaab', 'b'),
               ('aaaaa', 'a'),
               ('abcdefghij', 'a'),
               ('ababababababababab', 'b'),
            ]:
    print(f's, c = {s}, {c}')
    sol = Solution()
    r = sol.shortestToChar(s, c)
    print(f'r = {r}')
    print('=================')

