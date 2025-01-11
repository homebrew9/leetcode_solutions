from typing import List

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for op in logs:
            if op == '../':
                if cnt > 0:
                    cnt -= 1
            elif op == './':
                continue
            else:
                cnt += 1
        return cnt

# Main section
for logs in [
               ['d1/','d2/','../','d21/','./'],
               ['d1/','d2/','./','d3/','../','d31/'],
               ['d1/','../','../','../'],
               ['d1/','d2/','d3/','d4/','d5/','./','./','./','./','./','./','./','../','../','d6/'],
            ]:
    print(f'logs = {logs}')
    sol = Solution()
    r = sol.minOperations(logs)
    print(f'r = {r}')
    print('=================')

