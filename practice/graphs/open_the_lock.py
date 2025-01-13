from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def nextCombinations(s):
            res = list()
            # Next 4 combinations going forward
            for i in range(4):
                tmp = s[:i] + ('0' if s[i] == '9' else str(int(s[i])+1)) + s[i+1:]
                res.append(tmp)
            # Next 4 combinations going backward
            for i in range(4):
                tmp = s[:i] + ('9' if s[i] == '0' else str(int(s[i])-1)) + s[i+1:]
                res.append(tmp)
            return res
        dead = set(deadends)
        seen = set()
        start = '0000'
        if start in dead:
            return -1
        dq = deque()
        dq.append(start)
        seen.add(start)
        turns = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                cur = dq[0]
                if cur == target:
                    return turns
                for v in nextCombinations(cur):
                    if v not in seen and v not in dead:
                        dq.append(v)
                        seen.add(v)
                dq.popleft()
            turns += 1
        return -1

# Main section
for deadends, target in [
                           (['0201','0101','0102','1212','2002'], '0202'),
                           (['8888'], '0009'),
                           (['8887','8889','8878','8898','8788','8988','7888','9888'], '8888'),
                           (['0000'], '8888'),
                        ]:
    print(f'deadends, target = {deadends}, {target}')
    sol = Solution()
    r = sol.openLock(deadends, target)
    print(f'r = {r}')
    print('=======================')

