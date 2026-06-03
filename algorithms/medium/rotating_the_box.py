from typing import List

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = len(box)
        cols = len(box[0])
        for r in range(rows):
            row = box[r]
            i, j = cols - 1, cols - 1
            while i >= 0:
                if row[i] == '#':
                    row[i] = '.'
                    row[j] = '#'
                    j -= 1
                elif row[i] == '*':
                    j = i - 1
                i -= 1
        res = [[None for _ in range(rows)] for _ in range(cols)]
        r = 0
        for col in range(cols):
            c = 0
            for row in range(rows-1, -1, -1):
                res[r][c] = box[row][col] # type: ignore
                c += 1
            r += 1
        return res # type: ignore

# Main section
for box in [
              [['#','.','#']],
              [['#','.','*','.'],['#','#','*','.']],
              [['#','#','*','.','*','.'],['#','#','#','*','.','.'],['#','#','#','.','#','.']],
           ]:
    print(f'box = {box}')
    sol = Solution()
    r = sol.rotateTheBox(box)
    print(f'r = {r}')
    print('==============================')









