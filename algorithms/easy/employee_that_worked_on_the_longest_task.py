from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        hsh = dict()
        max_time = logs[0][1]
        hsh[max_time] = [logs[0][0]]
        
        for i in range(1, len(logs)):
            curr = logs[i][1] - logs[i-1][1]
            if curr >= max_time:
                max_time = curr
                if max_time in hsh:
                    hsh[max_time] += [logs[i][0]]
                else:
                    hsh = {}
                    hsh[max_time] = [logs[i][0]]
        print(f'\thsh = {hsh}')
        return min(list(hsh.values())[0])

# Main section
for n, logs in [
                  #(10, [[0,3],[2,5],[0,9],[1,15]]),
                  #(26, [[1,1],[3,7],[2,12],[7,17]]),
                  #(2, [[0,10],[1,20]]),
                  (70, [[36,3],[1,5],[12,8],[25,9],[53,11],[29,12],[52,14]]),
               ]:
    print(f'n, logs = {n}, {logs}')
    sol = Solution()
    r = sol.hardestWorker(n, logs)
    print(f'r = {r}')
    print('==========================')

