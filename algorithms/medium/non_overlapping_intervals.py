from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Greedy algorithm - See CLRS Section 16.1 Activity Selection Problem
        # Sort intervals by end time
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        res = 0
        for s, e in intervals[1:]:
            # If current interval is compatible, then reset end date;
            # otherwise remove current interval
            if s >= end:
                end = e
            else:
                res += 1
        return res

# Main section
for intervals in [
                    [[1,2],[2,3],[3,4],[1,3]],
                    [[1,2],[1,2],[1,2]],
                    [[1,2],[2,3]],
                    [[4,5],[-1,1],[-2,5],[-5,-4],[-2,0]],
                    [[-3,6],[-7,-3],[4,10],[-8,-3],[-7,1],[-5,6],[-10,-8],[5,6],[-2,2]],
                 ]:
    print(f'intervals = {intervals}')
    sol = Solution()
    r = sol.eraseOverlapIntervals(intervals)
    print(f'r = {r}')
    print('====================')


