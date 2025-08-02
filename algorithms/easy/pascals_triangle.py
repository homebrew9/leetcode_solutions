from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Recursive solution
        def solve(i):
            if i == 1:
                self.res.append([1])
                return
            solve(i - 1)
            arr = self.res[-1]
            tmp = [1] + [arr[j-1] + arr[j] for j in range(1, len(arr))] + [1]
            self.res.append(tmp)
        self.res = list()
        solve(numRows)
        return self.res

# Main section
for numRows in [
                   1,
                   2,
                   3,
                   4,
                   5,
                   10,
                   15,
                   20,
                   25,
                   30,
               ]:
    print(f'numRows = {numRows}')
    sol = Solution()
    r = sol.generate(numRows)
    print(f'r = {r}')
    print('==============')















