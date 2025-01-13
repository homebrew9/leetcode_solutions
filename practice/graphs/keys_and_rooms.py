#
# a) DFS recursive, b) DFS iterative, c) BFS
#
from typing import List
from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(r):
            if r in visited:
                return
            visited.add(r)
            for nr in rooms[r]:
                dfs(nr)
        visited = set()
        dfs(0)
        return len(visited) == len(rooms)
    def canVisitAllRooms_1(self, rooms: List[List[int]]) -> bool:
        def dfs(r):
            stack = list()
            stack.append(r)
            seen.add(r)
            while stack:
                cur = stack.pop()
                for nr in rooms[cur]:
                    if nr not in seen:
                        seen.add(nr)
                        stack.append(nr)
        seen = set()
        dfs(0)
        return len(seen) == len(rooms)
    def canVisitAllRooms_2(self, rooms: List[List[int]]) -> bool:
        def bfs(r):
            dq = deque()
            dq.append(r)
            seen.add(r)
            while dq:
                cur = dq.popleft()
                for nr in rooms[cur]:
                    if nr not in seen:
                        seen.add(nr)
                        dq.append(nr)
        seen = set()
        bfs(0)
        return len(seen) == len(rooms)

for rooms in [
                [[1],[2],[3],[]],
                [[1,3],[3,0,1],[2],[0]],
             ]:
    print(f'rooms = {rooms}')
    sol = Solution()
    r = sol.canVisitAllRooms(rooms)
    r1 = sol.canVisitAllRooms_1(rooms)
    r2 = sol.canVisitAllRooms_2(rooms)
    print(f'r (DFS recursion) = {r}')
    print(f'r1 (DFS stack)    = {r1}')
    print(f'r2 (BFS)          = {r2}')
    print('===================')


