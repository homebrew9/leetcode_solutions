from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        res = list()
        for i, interval in enumerate(intervals):
            # Case 1: interval lies to the left of newInterval
            # Eg. interval, newInterval = [3,5], [7,9]
            if interval[1] < newInterval[0]:
                res.append(interval)
            else:
                # Case 2: interval lies to the right of newInterval
                # Eg. interval, newInterval = [6,8], [2,5]
                if interval[0] > newInterval[1]:
                    return res + [newInterval] + intervals[i:]
                else:
                    # Case 3: interval and newInterval overlap in some way, eg.
                    # a) interval[0] <= newInterval[0] <= interval[1] or
                    # b) interval[0] <= newInterval[1] <= interval[1] or
                    # c) interval is entirely "inside" newInterval or
                    # d) newInterval is entirely "inside" interval etc.
                    newInterval[0] = min(newInterval[0], interval[0])
                    newInterval[1] = max(newInterval[1], interval[1])
        return res + [newInterval]

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



