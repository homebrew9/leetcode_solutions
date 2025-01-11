from typing import List
import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        if newInterval[1] == intervals[0][0]:
            intervals[0] = [newInterval[0], intervals[0][1]]
            return intervals
        if newInterval[0] == intervals[-1][1]:
            intervals[-1] = [intervals[-1][0], newInterval[1]]
            return intervals
        N = len(intervals)
        arr1 = [x for x, y in intervals]
        arr2 = [y for x, y in intervals]
        p, q = newInterval[0], newInterval[1]
        i = bisect.bisect_right(arr1, p)
        j = bisect.bisect_left(arr2, q)
        intvl = [0,0]
        if i == 0:
            left_chunk = []
            intvl[0] = p
        else:
            item1 = intervals[i-1]
            if p <= item1[1]:
                left_chunk = intervals[:i-1]
                intvl[0] = min(item1[0], p)
            else:
                left_chunk = intervals[:i]
                intvl[0] = p
        if j == 0:
            item2 = intervals[0]
            intvl[1] = max(item2[1], q)
            right_chunk = intervals[1:]
        elif j == N:
            item2 = intervals[-1]
            intvl[1] = max(item2[1], q)
            right_chunk = []
        else:
            item2 = intervals[j]
            if q >= item2[0]:
                right_chunk = intervals[j+1:]
                intvl[1] = max(item2[1], q)
            else:
                right_chunk = intervals[j:]
                intvl[1] = q
        #print(f'\t{left_chunk}, {intvl}, {right_chunk}')
        arr = left_chunk + [[intvl[0], intvl[1]]] + right_chunk
        return arr

# Main section
for intervals, newInterval in [
                                 ([[3,5],[6,7],[8,9]], [1,2]),
                                 ([[3,5],[6,7],[8,9]], [11,13]),
                                 ([[3,5],[6,7],[8,9]], [1,3]),
                                 ([[3,5],[6,7],[8,9]], [9,15]),
                                 ([[3,5],[7,9],[11,13]], [1,8]),
                                 ([[3,5],[7,9],[11,13]], [4,8]),
                                 ([[1,3],[6,9]], [2,5]),
                                 ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),
                                 ([[3,5],[7,9],[11,13]], [3,13]),
                                 ([[3,5],[7,9],[11,13]], [6,6]),
                                 ([[3,5],[7,9],[11,13]], [4,8]),
                                 ([[3,5],[7,9],[11,13]], [4,12]),
                                 ([[3,5],[7,9],[11,13]], [6,10]),
                                 ([[3,5],[7,9],[11,13]], [9,11]),
                                 ([[3,5],[7,9],[11,13]], [5,7]),
                                 ([[3,5],[7,9],[11,13]], [12,12]),
                                 ([[3,5],[7,9],[11,13]], [10,10]),
                                 ([[3,5],[7,9],[11,13]], [9,10]),
                                 ([], [5,7]),
                              ]:
    print(f'intervals, newInterval = {intervals}, {newInterval}')
    sol = Solution()
    r = sol.insert(intervals, newInterval)
    print(f'r = {r}')
    print('=============')

