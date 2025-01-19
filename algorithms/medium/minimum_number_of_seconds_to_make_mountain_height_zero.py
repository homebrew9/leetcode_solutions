from typing import List
from math import sqrt

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Given time t, if a worker with workerTime w destroys height x of the mountain, then:
        # t = w + (w*2) + (w*3) + ... + (w*x)
        # t = w * (1 + 2 + 3 + ... + x)
        # t = w * (x * (x + 1)) / 2, or
        # x^2 + x - (2*t/w) = 0
        # This is a quadratic equation for x, and solving it for x, we get:
        # x = (-1 + sqrt(1 + 8*t/w)) // 2
        # For a given t, we can find the total heights destroyed by all workers working simultaneously.
        # left bound of t is 0, right bound is the time take by worker with max workerTime.
        # Using Binary Search, we can zero in on the minimum such t.
        left = 0
        right = max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        ret = right
        while left <= right:
            t = (left + right) // 2
            height = 0
            for w in workerTimes:
                height += (-1 + sqrt(1 + (8 * t / w))) // 2
            if height >= mountainHeight:
                ret = min(ret, t)
                right = t - 1
            else:
                left = t + 1
        return ret

# Main section
for mountainHeight, workerTimes in [
                                      (4, [2,1,1]),
                                      (10, [3,2,2,4]),
                                      (5, [1]),
                                      (5, [1,2,3,4]),
                                   ]:
    print(f'mountainHeight, workerTimes = {mountainHeight}, {workerTimes}')
    sol = Solution()
    r = sol.minNumberOfSeconds(mountainHeight, workerTimes)
    print(f'r = {r}')
    print('==================')


