from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        q = [False] * n
        t1 = 0
        t2 = 0
        for i in range(n):
            if endTime[i] - startTime[i] <= t1:
                q[i] = True
            t1 = max(t1, startTime[i] - (0 if i == 0 else endTime[i - 1]))

            if endTime[n - i - 1] - startTime[n - i - 1] <= t2:
                q[n - i - 1] = True
            t2 = max(t2, (eventTime if i == 0 else startTime[n - i]) - endTime[n - i - 1])

        res = 0
        for i in range(n):
            left = 0 if i == 0 else endTime[i - 1]
            right = eventTime if i == n - 1 else startTime[i + 1]
            if q[i]:
                res = max(res, right - left)
            else:
                res = max(res, right - left - (endTime[i] - startTime[i]))
        return res

# Main section
for eventTime, startTime, endTime in [
                                        (5, [1,3], [2,5]),
                                        (10, [0,7,9], [1,8,10]),
                                        (10, [0,3,7,9], [1,4,8,10]),
                                        (5, [0,1,2,3,4], [1,2,3,4,5]),
                                     ]:
    print(f'eventTime, startTime, endTime = {eventTime}, {startTime}, {endTime}')
    sol = Solution()
    r = sol.maxFreeTime(eventTime, startTime, endTime)
    print(f'r = {r}')
    print('============================')






