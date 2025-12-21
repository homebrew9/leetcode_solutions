from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def dfs(src, adj):
            if src in visit:
                return
            visit.add(src)
            secrets.add(src)
            for nei in adj[src]:
                dfs(nei, adj)

        secrets = set([0, firstPerson]) # people with secrets
        time_map = dict() # time -> adj list meetings
        for src, dst, t in meetings:
            if t not in time_map:
                time_map[t] = defaultdict(list)
            time_map[t][src].append(dst)
            time_map[t][dst].append(src)

        for t in sorted(time_map.keys()):
            visit = set()
            for src in time_map[t]:
                if src in secrets:
                    dfs(src, time_map[t])
        return list(secrets)

# Main section
for n, meetings, firstPerson in [
                                   (6, [[1,2,5],[2,3,8],[1,5,10]], 1),
                                   (4, [[3,1,3],[1,2,2],[0,3,3]], 3),
                                   (5, [[3,4,2],[1,2,1],[2,3,1]], 1),
                                ]:
    print(f'n, meetings, firstPerson = {n}, {meetings}, {firstPerson}')
    sol = Solution()
    r = sol.findAllPeople(n, meetings, firstPerson)
    print(f'r = {r}')
    print('===========================')























































