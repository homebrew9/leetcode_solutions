from typing import List

class Solution:
    def pascals_rec(self, r, c, pt):
        #print(f'\t>>> r, c, pt = {r}, {c}, {pt}')
        if r == 0 or c == 0:
            pt[r][c] = 1
        elif pt[r][c] == 0:
            pt[r][c] = self.pascals_rec(r, c-1, pt) + self.pascals_rec(r-1, c, pt)
        return pt[r][c]

    def getRow(self, rowIndex: int) -> List[int]:
        global pt
        pt = list()
        for r in range(rowIndex+1):
            pt.append([])
            for c in range(rowIndex+1):
                pt[r].append(0)
        arr = list()
        for r in range(rowIndex, -1, -1):
            c = rowIndex - r
            val = self.pascals_rec(r, c, pt)
            arr.append(val)
        return arr

# Main section
sol = Solution()
for rowIndex in [
                   0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33
                ]:
    print(f'rowIndex = {rowIndex}')
    r = sol.getRow(rowIndex)
    print(f'r        = {r}')
    print('========================================')

