from typing import List
from math import inf

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_availability_time = [0] * n
        meeting_count = [0] * n
        for start, end in sorted(meetings):
            min_room_availability_time = inf
            min_available_time_room = 0
            found_unused_room = False
            for i in range(n):
                if room_availability_time[i] <= start:
                    found_unused_room = True
                    meeting_count[i] += 1
                    room_availability_time[i] = end
                    break
                if min_room_availability_time > room_availability_time[i]:
                    min_room_availability_time = room_availability_time[i]
                    min_available_time_room = i
            if not found_unused_room:
                room_availability_time[min_available_time_room] += end - start
                meeting_count[min_available_time_room] += 1

        return meeting_count.index(max(meeting_count))

# Main section
for n, meetings in [
                      (2, [[0,10],[1,5],[2,7],[3,4]]),
                      (3, [[1,20],[2,10],[3,5],[4,9],[6,8]]),
                   ]:
    print(f'n, meetings = {n}, {meetings}')
    sol = Solution()
    r = sol.mostBooked(n, meetings)
    print(f'r = {r}')
    print('============================')








