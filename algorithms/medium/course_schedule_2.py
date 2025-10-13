from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Kahn's Topological Sort.
        # A "cleaner" approach. We try to avoid dictionary modification here.
        children = defaultdict(list)
        indegree = defaultdict(int, {n: 0 for n in range(numCourses)})
        for a, b in prerequisites:
            children[b] += [a]
            indegree[a] += 1
        dq = deque([k for k, v in indegree.items() if v == 0])
        res = list()
        while dq:
            size = len(dq)
            for _ in range(size):
                curr = dq.popleft()
                res.append(curr)
                for child in children[curr]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        dq.append(child)
        return res if len(res) == numCourses else list()

# Main section
for numCourses, prerequisites in [
                                    (2, [[1,0]]),
                                    (4, [[1,0],[2,0],[3,1],[3,2]]),
                                    (1, []),
                                    (3, [[1,0],[1,2],[0,1]]),
                                 ]:
    print(f'numCourses, prerequisites = {numCourses}, {prerequisites}')
    sol = Solution()
    r = sol.findOrder(numCourses, prerequisites)
    print(f'r = {r}')
    print('=====================')


























