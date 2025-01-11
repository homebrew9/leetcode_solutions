from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        dq = deque()

        def getNextList(s):
            arr = list()
            for i in range(4):
                nextDigit = '0' if s[i] == '9' else str(int(s[i]) + 1)
                newNum = s[:i] + nextDigit + s[i+1:]
                if not newNum in visited and not newNum in deadends:
                    arr.append(newNum)
            for i in range(4):
                prevDigit = '9' if s[i] == '0' else str(int(s[i]) - 1)
                newNum = s[:i] + prevDigit + s[i+1:]
                if not newNum in visited and not newNum in deadends:
                    arr.append(newNum)
            return arr

        root = '0000'
        if root in deadends:
            return -1
        dq.append(root)
        visited.add(root)
        step = 0
        while dq:
            #print(f'\tdq = {dq}')
            size = len(dq)
            for i in range(size):
                cur = dq[0]
                if cur == target:
                    return step
                for v in getNextList(cur):
                    if not v in visited and not v in deadends:
                        dq.append(v)
                        visited.add(v)
                dq.popleft()
            step += 1

        return -1

# Main section
for deadends, target in [
                           (['0201','0101','0102','1212','2002'], '0202'),
                           (['0201','0101','0102','1212','2002'], '9999'),
                           (['8888'], '0009'),
                           (['8887','8889','8878','8898','8788','8988','7888','9888'], '8888'),
                           (['0000'], '8888'),
                        ]:
    print(f'deadends, target = {deadends}, {target}')
    sol = Solution()
    r = sol.openLock(deadends, target)
    print(f'r = {r}')
    print('==========================')

