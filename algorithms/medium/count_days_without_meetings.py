from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        N = len(meetings)
        meetings.sort()
        res = meetings[0][0] - 1
        for i in range(N):
            s, e = meetings[i]
            if i == 0:
                start, end = s, e
            else:
                if s <= end:
                    #start = min(start, s)
                    end = max(end, e)
                else:
                    res += s - end - 1
                    start, end = s, e
        res += days - end
        return res

# Main section
for days, meetings in [
                         (10, [[5,7],[1,3],[9,10]]),
                         (5, [[2,4],[1,3]]),
                         (6, [[1,6]]),
                         (57, [[3,49],[23,44],[21,56],[26,55],[23,52],[2,9],[1,48],[3,31]]),
                      ]:
    print(f'days, meetings = {days}, {meetings}')
    sol = Solution()
    r = sol.countDays(days, meetings)
    print(f'r = {r}')
    print('========================')

