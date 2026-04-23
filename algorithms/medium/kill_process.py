from collections import defaultdict
from typing import List

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        def dfs(node):
            self.res.append(node)
            for child in hsh[node]:
                dfs(child)
        hsh = defaultdict(list)
        self.res = list()
        for parent, child in zip(ppid, pid):
            if parent != 0:
                hsh[parent] += [child]
        dfs(kill)
        return self.res

# Main section
for pid, ppid, kill in [
                          ([1,3,10,5], [3,0,5,3], 5),
                          ([1], [0], 1),
                          ([1,2,3,4,5], [0,1,1,2,2], 1),
                          ([1,2,3,4,5], [0,1,1,2,2], 3),
                          ([1,2,3,4,5], [0,1,2,3,4], 2),
                          ([1,2,3,4,5,6], [0,1,1,1,1,1], 3),
                          ([1,2,3,4,5,6,7,8], [0,1,1,2,2,3,3,4], 2),
                          ([1,3,10,5,7,9], [0,1,1,3,3,5], 3),
                       ]:
    print(f'pid, ppid, kill = {pid}, {ppid}, {kill}')
    sol = Solution()
    r = sol.killProcess(pid, ppid, kill)
    print(f'r = {r}')
    print('==================================')
















