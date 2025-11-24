from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort by end ascending, and if equal, start descending
        intervals.sort(key=lambda x: (x[1], -x[0]))
        count = 0
        second_largest, largest = -1, -1
        for s, e in intervals:
            if s <= second_largest:
                # Both points are covered; skip
                continue
            if s <= largest:
                # One point covered, we need one; we pick e
                second_largest = largest
                largest = e
                count += 1
            else:
                # No coverage; we pick e-1 and e
                second_largest = e - 1
                largest = e
                count += 2
        return count

# Main section
for intervals in [
                    [[1,3],[3,7],[8,9]],
                    [[1,3],[1,4],[2,5],[3,5]],
                    [[1,2],[2,3],[2,4],[4,5]],
                 ]:
    print(f'intervals = {intervals}')
    sol = Solution()
    r = sol.intersectionSizeTwo(intervals)
    print(f'r = {r}')
    print('===========================')



