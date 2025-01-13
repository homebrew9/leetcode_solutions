from typing import List
from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(i, currTime):
            if i not in hsh:
                self.totalTime = max(self.totalTime, currTime)
                return
            for x in hsh[i]:
                dfs(x, currTime + informTime[i])
        hsh = defaultdict(list)
        for i, m in enumerate(manager):
            if m != -1:
                hsh[m] += [i]
        print(f'\thsh = {hsh}')
        self.totalTime = float('-inf')
        dfs(headID, 0)
        return self.totalTime

# Main section
for n, headID, manager, informTime in [
                                         (1, 0, [-1], [0]),
                                         (6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]),
                                         (15, 0, [-1,0,0,0,0,1,1,2,4,4,8,9,11,6,5], [1,2,2,0,3,3,1,0,2,1,0,4,0,0,0]),
                                         (11, 2, [2,2,-1,2,0,0,1,3,3,3,4], [2,1,1,3,4,0,0,0,0,0,0]),
                                      ]:
    print(f'n, headID, manager, informTime = {n}, {headID}, {manager}, {informTime}')
    sol = Solution()
    r = sol.numOfMinutes(n, headID, manager, informTime)
    print(f'r = {r}')
    print('===================')

