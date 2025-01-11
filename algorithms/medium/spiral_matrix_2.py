from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[None for _ in range(n)] for _ in range(n)]
        direction = 'right'
        r, c = 0, 0
        i = 1
        while True:
            if (r < 0 or r >= n) or (c < 0 or c >= n) or grid[r][c] is not None:
                break
            grid[r][c] = i
            i += 1
            if direction == 'right':
                if c == n-1 or grid[r][c+1] is not None:
                    direction = 'down'
                    r += 1
                else:
                    c += 1
            elif direction == 'down':
                if r == n-1 or grid[r+1][c] is not None:
                    direction = 'left'
                    c -= 1
                else:
                    r += 1
            elif direction == 'left':
                if c == 0 or grid[r][c-1] is not None:
                    direction = 'up'
                    r -= 1
                else:
                    c -= 1
            elif direction == 'up':
                if r == 0 or grid[r-1][c] is not None:
                    direction = 'right'
                    c += 1
                else:
                    r -= 1
        return grid

# Main section
for n in [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
         ]:
    print(f'n = {n}')
    sol = Solution()
    r = sol.generateMatrix(n)
    print(f'r = {r}')
    print('===================')


