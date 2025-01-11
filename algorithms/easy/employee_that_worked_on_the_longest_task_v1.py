#
# Hash is not required
#
from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_time = logs[0][1]
        min_id = logs[0][0]
        for i in range(1, len(logs)):
            curr = logs[i][1] - logs[i-1][1]
            if curr >= max_time:
                if curr == max_time:
                    min_id = min(min_id, logs[i][0])
                else:
                    min_id = logs[i][0]
                max_time = curr
        return min_id

# Main section
for n, logs in [
                  (10, [[0,3],[2,5],[0,9],[1,15]]),
                  (26, [[1,1],[3,7],[2,12],[7,17]]),
                  (2, [[0,10],[1,20]]),
                  (70, [[36,3],[1,5],[12,8],[25,9],[53,11],[29,12],[52,14]]),
               ]:
    print(f'n, logs = {n}, {logs}')
    sol = Solution()
    r = sol.hardestWorker(n, logs)
    print(f'r = {r}')
    print('==========================')


