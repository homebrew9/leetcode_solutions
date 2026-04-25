import bisect
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        left = [0] * n
        right = [0] * n
        num = [0] * n
        robots_to_distance = {}

        for i in range(n):
            robots_to_distance[robots[i]] = distance[i]

        robots.sort()
        walls.sort()

        for i in range(n):
            pos1 = bisect.bisect_right(walls, robots[i])

            if i >= 1:
                left_bound = max(
                    robots[i] - robots_to_distance[robots[i]], robots[i - 1] + 1
                )
                left_pos = bisect.bisect_left(walls, left_bound)
            else:
                left_pos = bisect.bisect_left(
                    walls, robots[i] - robots_to_distance[robots[i]]
                )

            left[i] = pos1 - left_pos

            if i < n - 1:
                right_bound = min(
                    robots[i] + robots_to_distance[robots[i]], robots[i + 1] - 1
                )
                right_pos = bisect.bisect_right(walls, right_bound)
            else:
                right_pos = bisect.bisect_right(
                    walls, robots[i] + robots_to_distance[robots[i]]
                )

            pos2 = bisect.bisect_left(walls, robots[i])
            right[i] = right_pos - pos2

            if i == 0:
                continue

            pos3 = bisect.bisect_left(walls, robots[i - 1])
            num[i] = pos1 - pos3

        sub_left, sub_right = left[0], right[0]
        for i in range(1, n):
            current_left = max(
                sub_left + left[i],
                sub_right - right[i - 1] + min(left[i] + right[i - 1], num[i]),
            )
            current_right = max(sub_left + right[i], sub_right + right[i])
            sub_left, sub_right = current_left, current_right

        return max(sub_left, sub_right)

# Main section
for robots, distance, walls in [
                                  ([4], [3], [1,10]),
                                  ([10,2], [5,1], [5,2,7]),
                                  ([1,2], [100,1], [10]),
                               ]:
    print(f'robots, distance, walls = {robots}, {distance}, {walls}')
    sol = Solution()
    r = sol.maxWalls(robots, distance, walls)
    print(f'r = {r}')
    print('==================================')













