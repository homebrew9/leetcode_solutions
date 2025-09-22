from typing import List

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min([s + t for s, t in tasks])

# Main section
for tasks in [
                [[1,6],[2,3]],
                [[100,100],[100,100],[100,100]],
             ]:
    print(f'tasks = {tasks}')
    sol = Solution()
    r = sol.earliestTime(tasks)
    print(f'r = {r}')
    print('===================')


