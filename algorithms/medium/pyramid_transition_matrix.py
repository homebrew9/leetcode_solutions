from collections import defaultdict
from typing import List
from functools import cache

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        pdic = defaultdict(list)
        for patt in allowed: pdic[patt[:2]].append(patt[2:])

        @cache
        def isgood(line):
            stack = ['z']*(len(line) -1)
            def nextline(depth):
                if  depth==len(stack):  return isgood(''.join(stack))
                for cube in pdic[line[depth] + line[depth+1]]:
                    stack[depth] = cube
                    if  nextline(depth+1):  return True
                return False
            return True if len(line) < 2  else nextline(0)
        return isgood(bottom)

# Main section
for bottom, allowed in [
                          ('BCD', ['BCC','CDE','CEA','FFF']),
                          ('AAAA', ['AAB','AAC','BCD','BBE','DEF']),
                       ]:
    print(f'bottom, allowed = {bottom}, {allowed}')
    sol = Solution()
    r = sol.pyramidTransition(bottom, allowed)
    print(f'r = {r}')
    print('========================')






















