from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # Let's use Kahn's Topological Sorting algorithm
        indegree = {k: 0 for k in range(1, n+1)}
        children = defaultdict(list)
        for prev_course, next_course in relations:
            children[prev_course] += [next_course]
            indegree[next_course] += 1
        dq = deque([k for k, v in indegree.items() if v == 0])
        res = list()
        semesters = 0
        while dq:
            size = len(dq)
            for _ in range(size):
                curr = dq.popleft()
                res.append(curr)
                for child in children[curr]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        dq.append(child)
            semesters += 1
        return -1 if len(res) != n else semesters

# Main section
for n, relations in [
                       (3, [[1,3],[2,3]]),
                       (3, [[1,2],[2,3],[3,1]]),
                    ]:
    print(f'n, relations = {n}, {relations}')
    sol = Solution()
    r = sol.minimumSemesters(n, relations)
    print(f'r = {r}')
    print('=====================')
















