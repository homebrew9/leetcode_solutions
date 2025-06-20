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

# Main section
for n, logs in [
                  (2, ['0:start:0','1:start:2','1:end:5','0:end:6']),
                  (1, ['0:start:0','0:start:2','0:end:5','0:start:6','0:end:6','0:end:7']),
                  (2, ['0:start:0','0:start:2','0:end:5','1:start:6','1:end:6','0:end:7']),
               ]:
    print(f'n, logs = {n}, {logs}')
    sol = Solution()
    r = sol.exclusiveTime(n, logs)
    print(f'r = {r}')
    print('===========================')








