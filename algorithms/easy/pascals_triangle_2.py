#
# Follow up: Algorithm uses only O(rowIndex) extra space.
#
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def fillNums(r, c):
            #print(f'\tr, c, lst = {r}, {c}, {self.lst}')
            if r > rowIndex:
                return
            if c == 0 or c == r:
                self.lst[c] = 1
            else:
                self.lst[c] = self.lst[c-1] + self.lst[c]
            if c == 0:
                fillNums(r+1, r+1)
            else:
                fillNums(r, c-1)
        self.lst = [None for _ in range(rowIndex+1)]
        fillNums(0, 0)
        return self.lst

# Main section
for rowIndex in [
                   0,
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
                   15,
                   20,
                   25,
                   30,
                   33,
                ]:
    print(f'rowIndex = {rowIndex}')
    sol = Solution()
    r = sol.getRow(rowIndex)
    print(f'r = {r}')
    print('==============')

