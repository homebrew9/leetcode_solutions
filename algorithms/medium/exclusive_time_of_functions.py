# =========================================================================================
# Both functions below use a stack. In the first function, we calculate the exclusive time
# of a function when it ends, and immediately subtract that time from the function at the
# top of stack. For example, if logs = ['0:start:0','1:start:4','1:end:7','0:end:10']
# then function 1 ran for 4 seconds [4,7]; we subtract 4 from function 0. Then
# function 0 ran for [0,10] minus exclusive time for function 1 i.e. 11 - 4 = 7 seconds.
# In the second function, we update function 0 as soon as we start function 1.
# =========================================================================================
from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0 for _ in range(n)]
        stack = list()
        for entry in logs:
            id, action, ts = entry.split(':')
            id, ts = int(id), int(ts)
            if action == 'start':
                stack.append([id, ts])
            else:
                idx, time = stack.pop()
                diff = ts - time + 1
                res[idx] += diff
                if len(stack) > 0:
                    ind = stack[-1][0]
                    res[ind] -= diff
        return res
    def exclusiveTime_1(self, n: int, logs: List[str]) -> List[int]:
        res = [0 for _ in range(n)]
        prev_ts = None
        stack = list()
        for entry in logs:
            id, action, ts = entry.split(':')
            id, ts = int(id), int(ts)
            if len(stack) == 0:
                stack.append([id, 1])
            else:
                diff = max(0, ts - prev_ts - 1)
                stack[-1][1] += diff
                if action == 'end':
                    idx, time = stack.pop()
                    if ts == prev_ts:
                        res[idx] += time
                    else:
                        res[idx] += time + 1
                else:
                    stack.append([id, 1])
            prev_ts = ts
        return res

# Main section
for n, logs in [
                  (2, ['0:start:0','1:start:2','1:end:5','0:end:6']),
                  (1, ['0:start:0','0:start:2','0:end:5','0:start:6','0:end:6','0:end:7']),
                  (2, ['0:start:0','0:start:2','0:end:5','1:start:6','1:end:6','0:end:7']),
               ]:
    print(f'n, logs = {n}, {logs}')
    sol = Solution()
    r = sol.exclusiveTime(n, logs)
    r1 = sol.exclusiveTime_1(n, logs)
    print(f'r  = {r}')
    print(f'r1 = {r1}')
    print('===========================')






