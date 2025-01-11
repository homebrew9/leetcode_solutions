from typing import List
from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Store all edges in "graph"
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        print(f'\tgraph = {graph}')

        # Store all nodes to be visited in "q"
        seen = [False] * n
        seen[source] = True
        q = deque([source])

        print(f'\tseen, q = {seen}, {q}')

        while q:
            print(f'\t\tseen, q = {seen}, {q}')
            curr_node = q.popleft()
            if curr_node == destination:
                return True

            # For each neighbor of curr_node, if we haven't visited it
            # before, then add it to q and mark it as visited
            for next_node in graph[curr_node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    q.append(next_node)

        return False

# Main section
for n, edges, source, destination in [
                                        (3, [[0,1],[1,2],[2,0]], 0, 2),
                                        (6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5),
                                     ]:
    print(f'n, edges, source, destination = {n}, {edges}, {source}, {destination}')
    sol = Solution()
    r = sol.validPath(n, edges, source, destination)
    print(f'r = {r}')
    print('====================')

