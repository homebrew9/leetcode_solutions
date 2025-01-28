from typing import List
from collections import deque, defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def is_prerequisite(a, b):
            dq = deque()
            seen = set()
            dq.append(a)
            seen.add(a)
            while dq:
                size = len(dq)
                for _ in range(size):
                    curr = dq.popleft()
                    if curr == b:
                        return True
                    for next_node in hsh[curr]:
                        if next_node not in seen:
                            dq.append(next_node)
                            seen.add(next_node)
            return False
        hsh = defaultdict(list)
        for u, v in prerequisites:
            hsh[u] += [v]
        res = list()
        for a, b in queries:
            res.append(is_prerequisite(a, b))
        return res

# Main section
for numCourses, prerequisites, queries in [
                                             (2, [[1,0]], [[0,1],[1,0]]),
                                             (2, [], [[1,0],[0,1]]),
                                             (3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]),
                                             (3, [[1,2],[2,0]], [[1,0],[1,2],[0,1]]),
                                          ]:
    print(f'numCourses, prerequisites, queries = {numCourses}, {prerequisites}, {queries}')
    sol = Solution()
    r = sol.checkIfPrerequisite(numCourses, prerequisites, queries)
    print(f'r = {r}')
    print('===================')


