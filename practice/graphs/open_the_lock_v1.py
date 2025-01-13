from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def nextTurns(s):
            N = len(s)
            res = list()
            for i in range(N):
                tmp = s[:i] + ('0' if s[i] == '9' else str(int(s[i])+1)) + s[i+1:]
                res.append(tmp)
                tmp = s[:i] + ('9' if s[i] == '0' else str(int(s[i])-1)) + s[i+1:]
                res.append(tmp)
            return res
        # Important note - converting the list into a set cuts down the runtime to a tenth.
        # With deadends list, runtime = 6751 ms.
        # With dead set, runtime = 662 ms.
        dead = set(deadends)
        dq = deque()
        seen = set()
        start = '0000'
        if start in dead:
            return -1
        dq.append(start)
        seen.add(start)
        steps = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                cur = dq[0]
                if cur == target:
                    return steps
                for t in nextTurns(cur):
                    if t not in dead and t not in seen:
                        seen.add(t)
                        dq.append(t)
                dq.popleft()
            steps += 1
        return -1

# Main section
for deadends, target in [
                           (['0201','0101','0102','1212','2002'], '0202'),
                           (['8888'], '0009'),
                           (['8887','8889','8878','8898','8788','8988','7888','9888'], '8888'),
                           (['0000'], '9999'),
                           (['8888'], '9999'),
                        ]:
    print(f'deadends, target = {deadends}, {target}')
    sol = Solution()
    r = sol.openLock(deadends, target)
    print(f'r = {r}')
    print('================')

  
