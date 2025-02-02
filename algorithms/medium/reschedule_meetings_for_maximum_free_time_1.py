from typing import List
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = list()
        if startTime[0] > 0:
            gaps.append(startTime[0])
        N = len(startTime)
        for i in range(1, N):
            gaps.append(startTime[i] - endTime[i-1])
        if endTime[-1] < eventTime:
            gaps.append(eventTime - endTime[-1])
        M = len(gaps)
        if M == 0:
            return 0
        # Sliding window
        res = 0
        curr = 0
        for i in range(M):
            if i <= k:
                curr += gaps[i]
            else:
                res = max(res, curr)
                curr -= gaps[i - k - 1]
                curr += gaps[i]
        res = max(res, curr)
        return res

# Main section
for eventTime, k, startTime, endTime in [
                                           (5, 1, [1,3], [2,5]),
                                           (10, 1, [0,2,9],  [1,4,10]),
                                           (5, 2, [0,1,2,3,4], [1,2,3,4,5]),
                                           (227, 3, [12,16,215,222], [14,201,219,225]),
                                           (21, 1, [7,10,16], [10,14,18]),
                                        ]:
    print(f'eventTime, k, startTime, endTime = {eventTime}, {k}, {startTime}, {endTime}')
    sol = Solution()
    r = sol.maxFreeTime(eventTime, k, startTime, endTime)
    print(f'r = {r}')
    print('======================')

