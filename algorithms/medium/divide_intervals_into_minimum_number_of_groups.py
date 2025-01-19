#
# Very similar to the problem "Meeting Rooms II"
#
from typing import List
from sortedcontainers import SortedList

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals.sort()
        sl = SortedList([intervals[0][1]])
        res = 1
        for s, e in intervals[1:]:
            while sl and s > sl[0]:
                sl.pop(0)
            sl.add(e)
            res = max(res, len(sl))
        return res

# Main section
for intervals in [
                    [[5,10],[6,8],[1,5],[2,3],[1,10]],
                    [[1,3],[5,6],[8,10],[11,13]],
                    [[870474,950951]],
                    [[177246,301554],[311218,466819],[668516,998559],[893646,993889],[812820,874057],[629721,687595],[444283,642262],[451914,657216],[770537,816936],[507208,708085],[854030,952288],[527560,714801],[463050,856876],[129440,835130],[88421,867500],[715575,812634],[401547,564373],[592516,923611],[420084,611301],[852048,993781],[526338,751298],[402359,752631],[995715,997998],[656450,920519]],
                 ]:
    print(f'intervals = {intervals}')
    sol = Solution()
    r = sol.minGroups(intervals)
    print(f'r = {r}')
    print('======================')


