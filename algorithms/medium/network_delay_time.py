from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's Algorithm with just a dictionary of all nodes
        hsh = defaultdict(list)
        for u, v, w in times:
            hsh[u] += [(v, w)]
        # Each tuple in the Min Heap is of form: (total time from source to node, node)
        h = list()
        heapq.heapify(h)
        heapq.heappush(h, (0, k))
        min_times = defaultdict(int)
        while h:
            time_taken, node = heapq.heappop(h)
            if node in min_times:
                continue
            min_times[node] = time_taken
            for next_node, next_time in hsh[node]:
                heapq.heappush(h, (time_taken + next_time, next_node))
        if len(min_times) != n:
            return -1
        return max(min_times.values())

# Main section
for times, n, k in [
                      ([[1,2,1],[1,3,1],[1,4,2]], 4, 1),
                      ([[1,2,1],[1,3,1],[1,4,2],[2,5,2],[3,5,3],[3,6,4],[4,6,1]], 6, 1),
                      ([[1,2,1],[1,3,1],[1,4,2],[2,5,2],[3,5,3],[3,6,4],[4,6,1],[5,7,4],[6,8,3]], 8, 1),
                      ([[2,1,1],[2,3,1],[3,4,1]], 4, 2),
                      ([[1,2,1]], 2, 1),
                      ([[1,2,1]], 2, 2),
                      ([[1,2,1],[2,3,2],[4,5,2]], 5, 1),
                      ([[1,2,1],[2,1,3]], 2, 2),
                   ]:
    print(f'times, n, k = {times}, {n}, {k}')
    sol = Solution()
    r = sol.networkDelayTime(times, n, k)
    print(f'r = {r}')
    print('==================')


