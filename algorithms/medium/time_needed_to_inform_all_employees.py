#
# Wrong answer for last test case! However, from the defaultdict, it seems correct.
#
from typing import List
from collections import defaultdict, deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        hsh = defaultdict(list)
        for i, v in enumerate(manager):
            if v != -1:
                hsh[v] += [i]
        print(f'\thsh = {hsh}')
        res = informTime[headID]
        arr = [headID]
        dq = deque()
        while True:
            for i in arr:
                if i in hsh:
                    dq += hsh[i]
            if len(dq) == 0:
                break
            arr = []
            curr = 0
            while dq:
                k = dq.popleft()
                if k in hsh:
                    curr = max(curr, informTime[k])
                arr.append(k)
            res += curr
        return res

# Main section
for n, headID, manager, informTime in [
        #(1, 0, [-1], [0]),
        #(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]),
        #(9, 2, [2,2,-1,2,0,1,0,8,3], [2,3,1,5,11,4,9,3,3]),
        (11, 4, [5,9,6,10,-1,8,9,1,9,3,4], [0,213,0,253,686,170,975,0,261,309,337]),
    ]:
    print(f'n, headId, manager, informTime = {n}, {headID}, {manager}, {informTime}')
    sol = Solution()
    r = sol.numOfMinutes(n, headID, manager, informTime)
    print(f'r = {r}')
    print('=====================')

