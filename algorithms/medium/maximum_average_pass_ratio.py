from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        N = len(classes)
        # Each element of the max heap is of form: (-diff, index)
        # where diff is the delta decrease when (x/y) turns into (x+1)/(y+1)
        # We need to keep picking the max diff and add 1 extra student each time to it.
        h = [(x/y - (x+1)/(y+1), i) for i, (x, y) in enumerate(classes)]
        heapq.heapify(h)
        for _ in range(extraStudents):
            _, i = heapq.heappop(h)
            x, y = classes[i][0]+1, classes[i][1]+1
            classes[i] = [x, y]
            heapq.heappush(h, (x/y - (x+1)/(y+1), i))
        total = sum([x/y for x, y in classes])
        return total / N

# Main section
for classes, extraStudents in [
                                 ([[1,2],[3,5],[2,2]], 2),
                                 ([[2,4],[3,9],[4,5],[2,10]], 4),
                              ]:
    print(f'classes, extraStudents = {classes}, {extraStudents}')
    sol = Solution()
    r = sol.maxAverageRatio(classes, extraStudents)
    print(f'r = {r}')
    print('===================')


