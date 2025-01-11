from typing import List
import bisect

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        def dfs(cur_index, count):
            # dfs(i, c) is the maximum value obtained by attending a maximum of c events
            # in the range events[i ~ n-1]
            if count == 0 or cur_index == N:
                return 0
            if dp[count][cur_index] is not None:
                return dp[count][cur_index]
            val1 = dfs(cur_index + 1, count)
            # Binary Search to find the next index
            next_index = bisect.bisect_right(starts, events[cur_index][1])
            val2 = dfs(next_index, count-1) + events[cur_index][2]
            max_val = max(val1, val2)
            dp[count][cur_index] = max_val
            return dp[count][cur_index]
            
        N = len(events)
        events.sort()
        starts = [start for start, _, _ in events]
        dp = [[None for _ in range(N)] for _ in range(k+1)]
        return dfs(0, k)

# Main section
for events, k in [
                    ([[1,2,4],[3,4,3],[2,3,1]], 2),
                    ([[1,2,4],[3,4,3],[2,3,10]], 2),
                    ([[1,1,1],[2,2,2],[3,3,3],[4,4,4]], 3),
                 ]:
    print(f'events, k = {events}, {k}')
    sol = Solution()
    r = sol.maxValue(events, k)
    print(f'r = {r}')
    print('================')

