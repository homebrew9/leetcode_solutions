from typing import List
from functools import cache

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        @cache
        def dfs(r, f, used):
            if r == R: # assigned all robots
                return 0
            if f == F: # out of factories
                return MAX
            if used == factory[f][1]: # the factory is exhausted -> try next one
                return dfs(r, f + 1, 0)
            pick = abs(robot[r] - factory[f][0]) + dfs(r + 1, f, used + 1)
            skip = dfs(r, f + 1, 0)
            return min(pick, skip)
        
        MAX = 10**20
        R = len(robot)
        F = len(factory)
        robot.sort()
        factory.sort()
        return dfs(0, 0, 0)

# Main section
for robot, factory in [
                         ([0,4,6], [[2,2],[6,2]]),
                         ([1,-1], [[-2,1],[2,1]]),
                      ]:
    print(f'robot, factory = {robot}, {factory}')
    sol = Solution()
    r = sol.minimumTotalDistance(robot, factory)
    print(f'r = {r}')
    print('==================================')






