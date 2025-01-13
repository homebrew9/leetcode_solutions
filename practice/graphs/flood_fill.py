from typing import List
from collections import deque
from copy import deepcopy

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Recursive DFS
        def dfs(r, c, prevColor, color):
            if r < 0 or r >= rows:
                return
            if c < 0 or c >= cols:
                return
            if image[r][c] != prevColor:
                return
            if (r, c) in seen:
                return
            image[r][c] = color
            seen.add((r, c))
            for dr, dc in directions:
                dfs(r+dr, c+dc, prevColor, color)
        if image[sr][sc] == color:
            return image
        rows = len(image)
        cols = len(image[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        prevColor = image[sr][sc]
        seen = set()
        dfs(sr, sc, prevColor, color)
        return image
    def floodFill_1(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Iterative DFS using stack
        def dfs(r, c, prevColor, color):
            stack = list()
            stack.append((r, c))
            seen.add((r, c))
            while stack:
                cur = stack.pop()
                image[cur[0]][cur[1]] = color
                for dr, dc in directions:
                    rnew = cur[0] + dr
                    cnew = cur[1] + dc
                    if 0 <= rnew < rows and 0 <= cnew < cols:
                        if image[rnew][cnew] == prevColor and (rnew, cnew) not in seen:
                            stack.append((rnew, cnew))
                            seen.add((rnew, cnew))
        if image[sr][sc] == color:
            return image
        rows = len(image)
        cols = len(image[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        prevColor = image[sr][sc]
        seen = set()
        dfs(sr, sc, prevColor, color)
        return image
    def floodFill_2(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # BFS
        def bfs(r, c, prevColor, color):
            dq = deque()
            dq.append((r, c))
            seen.add((r, c))
            while dq:
                size = len(dq)
                for _ in range(size):
                    r1, c1 = dq.popleft()
                    image[r1][c1] = color
                    for dr, dc in directions:
                        rnew = r1 + dr
                        cnew = c1 + dc
                        if 0 <= rnew < rows and 0 <= cnew < cols:
                            if image[rnew][cnew] == prevColor and (rnew, cnew) not in seen:
                                dq.append((rnew, cnew))
                                seen.add((rnew, cnew))
        if image[sr][sc] == color:
            return image
        rows = len(image)
        cols = len(image[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        prevColor = image[sr][sc]
        seen = set()
        bfs(sr, sc, prevColor, color)
        return image

# Main section
# Notice that we create deep copies of image because it is updated in each function call!
for image, sr, sc, color in [
                              ([[1,0,0],[1,1,0],[1,0,1]], 1, 1, 9),
                              ([[1,0,0],[1,1,0],[1,0,1]], 1, 1, 1),
                              ([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2),
                              ([[0,0,0],[0,0,0]], 0, 0, 0),
                            ]:
    print(f'image, sr, sc, color = {image}, {sr}, {sc}, {color}')
    image_1 = deepcopy(image)
    image_2 = deepcopy(image)
    sol = Solution()
    r = sol.floodFill(image, sr, sc, color)
    r1 = sol.floodFill_1(image_1, sr, sc, color)
    r2 = sol.floodFill_2(image_2, sr, sc, color)
    print(f'r  (DFS Recursive) = {r}')
    print(f'r1 (DFS Iterative) = {r1}')
    print(f'r2 (BFS)           = {r2}')
    assert(r == r1)
    assert(r1 == r2)
    assert(r == r2)
    print('==================')


