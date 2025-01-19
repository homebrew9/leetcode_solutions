#
# Make sure to understand the working of Kahn's Topological Sort (KTS) Algorithm
# from this link: https://leetcode.com/problems/course-schedule/solution/
# Very nice, intuitive diagram!
# Given below is a crude implementation of the algorithm that aids us in
# finding cycles. The KTS algorithm can (among other things?) help us in finding
# cycles. It can be implemented by BFS, DFS or separately.
#

from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's Topological Sort using BFS
        arr = [[0,0] for _ in range(numCourses)]
        hsh = defaultdict(list)
        for a, b in prerequisites:
            hsh[a] += [b]
            arr[a][1] += 1
            arr[b][0] += 1
        dq = deque()
        seen = set()
        for i in range(numCourses):
            if arr[i][0] == 0:
                dq.append(i)
                seen.add(i)
        while dq:
            size = len(dq)
            for _ in range(size):
                curr = dq.popleft()
                for v in hsh[curr]:
                    arr[v][0] -= 1
                arr[curr][1] -= 1
                del hsh[curr]
            for i in range(numCourses):
                if arr[i][0] == 0 and i not in seen:
                    dq.append(i)
                    seen.add(i)
        res = 0
        for i in range(numCourses):
            if arr[i][0] == 0:
                res += 1
        return res == numCourses

# Main section
for numCourses, prerequisites in [
                                   (7, [[1,2],[2,4],[4,3],[3,2],[5,3]]),
                                   (7, [[0,1],[0,2],[1,3],[2,3],[4,5],[4,6]]),
                                   (5, [[1,4],[2,4],[3,1],[3,2]]),
                                   (20, [[0,10],[3,18],[5,5],[6,11],[11,4],[13,1],[15,1],[17,4]]),
                                   (1, []),
                                   (2, [[1,0]]),
                                   (5, [[1,2],[2,3],[3,4],[4,1]]),
                                 ]:
    print(f'numCourses, prerequisites = {numCourses}, {prerequisites}')
    sol = Solution()
    r = sol.canFinish(numCourses, prerequisites)
    print(f'r = {r}')
    print('===================')


