from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = list()
        x = [1]
        y = list()
        ret.append(x)
        for i in range(numRows-1):
            y = [1] + [ x[j]+x[j+1] for j in range(len(x)-1)] + [1]
            ret.append(y)
            x = y
        return ret 

# Main section
sol = Solution()
for nrows in [
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
             ]:
    print(f'nrows = {nrows}')
    r = sol.generate(nrows)
    print(f'r     = {r}')
    print('=====================================')


