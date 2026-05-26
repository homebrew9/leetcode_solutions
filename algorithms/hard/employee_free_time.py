import heapq

# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None): # type: ignore
        self.start = start
        self.end = end

class Solution(object):
    def employeeFreeTime(self, avails):
        ans = []
        pq = [(emp[0].start, ei, 0) for ei, emp in enumerate(avails)]
        heapq.heapify(pq)
        anchor = min(iv.start for emp in avails for iv in emp)
        while pq:
            t, e_id, e_jx = heapq.heappop(pq)
            if anchor < t:
                ans.append(Interval(anchor, t))
            anchor = max(anchor, avails[e_id][e_jx].end)
            if e_jx + 1 < len(avails[e_id]):
                heapq.heappush(pq, (avails[e_id][e_jx+1].start, e_id, e_jx+1))

        return ans

## Main section
#for schedule in [
#                   [[[1,2],[5,6]],[[1,3]],[[4,10]]],
#                   [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]],
#                ]:
#    print(f'schedule = {schedule}')
#    avails = [[Interval(start, end) for start, end in schedule[0]]]
#    sol = Solution()
#    #r = sol.employeeFreeTime(schedule)
#    r = sol.employeeFreeTime(avails)
#    print([(obj.start, obj.end) for obj in r])
#    print(f'r = {r}')
#    print('==================================')












