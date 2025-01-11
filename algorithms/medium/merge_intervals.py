from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        curr = None
        for i in sorted(intervals):
            if curr is None:
                curr = i
            elif i[0] <= curr[1]:
                curr = [curr[0], max(curr[1], i[1])]
            else:
                res += [curr]
                curr = i
        res += [curr]
        return res

# Main section
for intervals in [
                    [[1,3],[2,6],[8,10],[15,18]],
                    [[1,4],[4,5]],
                    [[1,9],[2,5],[19,20],[10,11],[12,20],[0,3],[0,1],[0,2]],
                 ]:
    print(f'intervals = {intervals}')
    sol = Solution()
    r = sol.merge(intervals)
    print(f'r = {r}')
    print('====================')

