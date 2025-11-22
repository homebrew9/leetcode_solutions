from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = list()
        res = [0] * n
        prev = None
        for i in range(len(logs)):
            id, event, ts = logs[i].split(':')
            id, ts = int(id), int(ts)
            if i == 0:
                stack.append(id)
                prev = ts
            elif event == 'start':
                if stack:
                    res[stack[-1]] += ts - prev # type: ignore
                stack.append(id)
                prev = ts
            else:
                res[stack[-1]] += ts - prev + 1 # type: ignore
                stack.pop()
                prev = ts + 1
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






