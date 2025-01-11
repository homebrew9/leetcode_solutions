from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        # ===========================================
        # CAUTION: DO NOT DO THE FOLLOWING!!!!!
        #self.vis = [[False] * cols] * rows]
        # ===========================================
        self.vis = [[False for _ in range(cols)] for _ in range(rows)]
        self.old_value = image[sr][sc]

        def dfs(image, rows, cols, r, c, k):
            #print(f'\trows, cols, r, c, k = {rows}, {cols}, {r}, {c}, {k} ; image = {image} ; vis = {self.vis}\n')
            if r < 0 or r > rows - 1:
                return
            if c < 0 or c > cols - 1:
                return
            if self.vis[r][c]:
                return
            if image[r][c] != self.old_value:
                return
            image[r][c] = k
            self.vis[r][c] = True
            dfs(image, rows, cols, r-1, c, k)
            dfs(image, rows, cols, r+1, c, k)
            dfs(image, rows, cols, r, c+1, k)
            dfs(image, rows, cols, r, c-1, k)

        dfs(image, rows, cols, sr, sc, color)
        return image

# Main section
for image, sr, sc, color in [
                               ([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2),
                               ([[0,0,0],[0,0,0]], 0, 0, 0),
                            ]:
    print(f'image = {image} ; sr, sc, color = {sr}, {sc}, {color}')
    sol = Solution()
    r = sol.floodFill(image, sr, sc, color)
    print(f'r = {r}')
    print('==========================')

