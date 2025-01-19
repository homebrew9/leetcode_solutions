from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        h = []
        heapq.heapify(h)
        res = 0
        N = len(intervals)
        heapq.heappush(h, intervals[0][1])
        res = max(res, len(h))
        for i in range(1, N):
            start, end = intervals[i]
            while len(h) > 0 and start >= h[0]:
                heapq.heappop(h)
            heapq.heappush(h, end)
            res = max(res, len(h))
        return res

# Main section
for intervals in [
                    [[0,30],[5,10],[15,20]],
                    [[7,10],[2,4]],
                    [[5,10],[6,8],[1,5],[2,3],[1,10]],
                    [[1,3],[5,6],[8,10],[11,13]],
                    [[870474,950951]],
                    [[177246,301554],[311218,466819],[668516,998559],[893646,993889],[812820,874057],[629721,687595],[444283,642262],[451914,657216],[770537,816936],[507208,708085],[854030,952288],[527560,714801],[463050,856876],[129440,835130],[88421,867500],[715575,812634],[401547,564373],[592516,923611],[420084,611301],[852048,993781],[526338,751298],[402359,752631],[995715,997998],[656450,920519]],
                 ]:
    print(f'intervals = {intervals}')
    sol = Solution()
    r = sol.minMeetingRooms(intervals)
    print(f'r = {r}')
    print('======================')


