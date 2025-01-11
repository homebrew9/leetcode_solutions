#
# Too complicated and buggy!! Does not work for most of the testcases.
# We can **UPDATE** the newInterval as we go through the "intervals" list;
# that will make the process much simpler! Check the next version.
#
from typing import List
import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        p, q = newInterval
        left, right = p, q
        i, j = 0, 0
        while i < N:
            x, y = intervals[i]
            if q < x:
                j = i
                break
            if x <= q <= y:
                left = min(p, x)
                j = i + 1
                right = max(q, y)
                break
            if x <= p <= y:
                left = min(p, x)
                j = i + 1
                if x <= q <= y:
                    right = max(q, y)
                    break
                while j < N:
                    r, s = intervals[j]
                    right = q
                    if q < r:
                        right = q
                        break
                    if r <= q <= s:
                        right = max(q, s)
                        j += 1
                        break
                    j += 1
            i += 1
        left_chunk = intervals[:i]
        right_chunk = intervals[j:]
        #print(f'\t{left_chunk}, {right_chunk}')
        return left_chunk + [[left, right]] + right_chunk

# Main section
for intervals, newInterval in [
                                 ([[3,5],[6,7],[8,9]], [1,2]),
                                 ([[3,5],[6,7],[8,9]], [11,13]),
                                 ([[3,5],[6,7],[8,9]], [1,3]),
                                 #([[3,5],[6,7],[8,9]], [9,15]),
                                 #([[3,5],[7,9],[11,13]], [1,8]),
                                 #([[3,5],[7,9],[11,13]], [4,8]),
                                 #([[1,3],[6,9]], [2,5]),
                                 #([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),
                                 #([[3,5],[7,9],[11,13]], [3,13]),
                                 #([[3,5],[7,9],[11,13]], [6,6]),
                                 #([[3,5],[7,9],[11,13]], [4,8]),
                                 #([[3,5],[7,9],[11,13]], [4,12]),
                                 #([[3,5],[7,9],[11,13]], [6,10]),
                                 #([[3,5],[7,9],[11,13]], [9,11]),
                                 #([[3,5],[7,9],[11,13]], [5,7]),
                                 #([[3,5],[7,9],[11,13]], [12,12]),
                                 #([[3,5],[7,9],[11,13]], [10,10]),
                                 #([[3,5],[7,9],[11,13]], [9,10]),
                                 #([], [5,7]),
                              ]:
    print(f'intervals, newInterval = {intervals}, {newInterval}')
    sol = Solution()
    r = sol.insert(intervals, newInterval)
    print(f'r = {r}')
    print('=============')


