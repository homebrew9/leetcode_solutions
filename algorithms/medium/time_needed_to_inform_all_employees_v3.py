#
# Solution using heap or SortedList. Default heap in Python is minheap, so pop() removes
# the min element. SortedList is sorted ascending by default, so to pop min, we use the
# pop(index=0) method in SortedList.
#
from typing import List
import heapq
from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        hsh = defaultdict(list)
        for i, v in enumerate(manager):
            if v != -1:
                hsh[v] += [i]
        #print(f'\thsh = {hsh}')
        h = [(0, headID)]
        heapq.heapify(h)
        maxTime = 0
        while h:
            timeSoFar, node = heapq.heappop(h)
            maxTime = max(maxTime, timeSoFar)
            for x in hsh[node]:
                heapq.heappush(h, (informTime[node] + timeSoFar, x))
        return maxTime
    #def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    #    hsh = defaultdict(list)
    #    for i, v in enumerate(manager):
    #        if v != -1:
    #            hsh[v] += [i]
    #    #print(f'\thsh = {hsh}')
    #    sl = SortedList([(0, headID)])
    #    #print(f'\tsl = {sl}')
    #    maxTime = 0
    #    while sl:
    #        (timeSoFar, node) = sl.pop(index=0)
    #        maxTime = max(maxTime, timeSoFar)
    #        for x in hsh[node]:
    #            sl.add((informTime[node] + timeSoFar, x))
    #    return maxTime

# Main section
for n, headID, manager, informTime in [
        (1, 0, [-1], [0]),
        (6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]),
        (9, 2, [2,2,-1,2,0,1,0,8,3], [2,3,1,5,0,0,0,0,3]),
        (11, 4, [5,9,6,10,-1,8,9,1,9,3,4], [0,213,0,253,686,170,975,0,261,309,337]),
        (11, 0, [-1,0,1,1,1,2,2,3,4,4,7], [1,2,4,10,2,0,0,1,0,0,0]),
        (15, 0, [-1,0,0,0,0,1,1,2,4,4,8,9,11,6,5], [1,2,2,0,3,3,1,0,2,1,0,4,0,0,0]),
        (11, 2, [2,2,-1,2,0,0,1,3,3,3,4], [2,1,1,3,4,0,0,0,0,0,0]),
    ]:
    print(f'n, headId, manager, informTime = {n}, {headID}, {manager}, {informTime}')
    sol = Solution()
    r = sol.numOfMinutes(n, headID, manager, informTime)
    print(f'r = {r}')
    print('=====================')


