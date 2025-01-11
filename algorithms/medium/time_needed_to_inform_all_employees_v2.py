#
# Original idea about passing a "path" array threw TLE. So let's try to send
# only the max time so far!
#
from typing import List
from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(node, time_so_far):
            if node not in hsh:
                #print(arr)
                #print([informTime[i] for i in arr[:-1]])
                #print(sum([informTime[i] for i in arr[:-1]]))
                #print('=====')
                #totalTime = sum([informTime[i] for i in arr])
                self.timeNeeded = max(self.timeNeeded, time_so_far)
                return
            for sub in hsh[node]:
                dfs(sub, time_so_far + informTime[sub])
        hsh = defaultdict(list)
        for i, v in enumerate(manager):
            if v != -1:
                hsh[v] += [i]
        #print(hsh)
        self.timeNeeded = float('-inf')
        #arr = list()
        #arr.append(headID)
        time_so_far = informTime[headID]
        dfs(headID, time_so_far)
        return self.timeNeeded

# Main section
for n, headID, manager, informTime in [
        (1, 0, [-1], [0]),
        (6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]),
        (9, 2, [2,2,-1,2,0,1,0,8,3], [2,3,1,5,0,0,0,0,3]),
        (11, 4, [5,9,6,10,-1,8,9,1,9,3,4], [0,213,0,253,686,170,975,0,261,309,337]),
        (11, 0, [-1,0,1,1,1,2,2,3,4,4,7], [1,2,4,10,2,0,0,1,0,0,0]),
    ]:
    print(f'n, headId, manager, informTime = {n}, {headID}, {manager}, {informTime}')
    sol = Solution()
    r = sol.numOfMinutes(n, headID, manager, informTime)
    print(f'r = {r}')
    print('=====================')

