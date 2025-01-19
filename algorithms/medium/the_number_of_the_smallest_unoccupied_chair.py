from typing import List
import heapq
from sortedcontainers import SortedList

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        N = len(times)
        # Arrival = 1, Departure = 0
        sl = SortedList([(a, 1, i) for i, (a, d) in enumerate(times)] + [(d, 0, i) for i, (a, d) in enumerate(times)])
        friends = [None for _ in range(N)]
        h = [i for i in range(N)]
        heapq.heapify(h)
        for _, activity, i in sl:
            if activity == 1:
                ch = heapq.heappop(h)
                if i == targetFriend:
                    return ch
                friends[i] = ch
            elif activity == 0:
                ch = friends[i]
                heapq.heappush(h, ch)
                friends[i] = None

# Main section
for times, targetFriend in [
                              ([[1,4],[2,3],[4,6]], 1),
                              ([[3,10],[1,5],[2,6]], 0),
                           ]:
    print(f'times, targetFriend = {times}, {targetFriend}')
    sol = Solution()
    r = sol.smallestChair(times, targetFriend)
    print(f'r = {r}')
    print('==================')


