'''
3341. Find Minimum Time to Reach Last Room I (Medium)
=====================================================
moveTime =
[[0,1,4],
 [2,1,3],
 [4,2,1],
 [1,1,4]]
moveTime =
[[0,1,1],
 [2,1,30],
 [5,20,1],
 [1,1,4]]
'''
from typing import List
import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows = len(moveTime)
        cols = len(moveTime[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        h = list()
        #seen = set()
        heapq.heapify(h)  # Each element of heap = (time_taken_to_reach_here, row, col)
        heapq.heappush(h, (0,0,0))
        #seen.add((0,0,0))
        arrivalTime = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        while h:
            #print(f'\th = {h}')
            t, r, c = heapq.heappop(h)
            if r == rows - 1 and c == cols - 1:
                return t
            for dr, dc in directions:
                rnew = r + dr
                cnew = c + dc
                if 0 <= rnew < rows and 0 <= cnew < cols:
                    if t >= moveTime[rnew][cnew]:
                        tnew = t + 1
                    else:
                        tnew = moveTime[rnew][cnew] + 1
                    #if (tnew, rnew, cnew) not in seen:     # <== this results in an infinite loop
                    #    seen.add((tnew, rnew, cnew))
                    #    heapq.heappush(h, (tnew, rnew, cnew))
                    if tnew < arrivalTime[rnew][cnew]:
                        arrivalTime[rnew][cnew] = tnew
                        heapq.heappush(h, (tnew, rnew, cnew))

# Main section
for moveTime in [
                   [[0,1,4],[2,1,3],[4,2,1],[1,1,4]],
                   [[0,1,1],[2,1,30],[5,20,1],[1,1,4]],
                   [[36,1,59,12,24],[41,28,6,28,25],[11,61,24,6,3],[52,31,57,30,49],[45,53,68,32,17]],
                   [[529,764,728,714,734,158,314,85,604,479],[164,757,140,587,783,436,839,211,253,876],[858,987,352,882,18,784,228,61,852,427],[552,497,159,464,280,386,820,311,671,368],[298,395,852,316,460,617,235,949,980,621],[237,368,311,171,753,46,542,297,631,15],[299,907,830,26,178,258,147,349,117,923],[245,114,533,527,642,455,969,192,351,287],[579,823,168,888,875,634,702,250,796,118],[596,433,594,993,466,772,267,97,144,704]],
                   [[6,37,33,67,8,43,3,63,59,65],[59,34,46,46,41,41,42,10,6,33],[24,64,59,69,22,30,2,2,28,28],[14,2,67,53,41,22,3,61,7,8],[47,55,62,25,23,50,35,26,10,44]],
                   [[0,126969709,692032326,92053731,508551731,859810360,388729349,57640450,841677654,739014179,467138675,94615502,952632759,252430470,835736786,86361012,965714421,385842975,624261617,495635069],[228590536,19827562,80076016,724173903,602876749,646209287,363055355,708072009,854752594,379049687,878179195,103958121,283661589,165703337,951810609,561641008,954446715,605519440,44995147,0]],
                   [[94,79,62,27,69,84],[6,32,11,82,42,30]],
                ]:
    print(f'moveTime = {moveTime}')
    sol = Solution()
    r = sol.minTimeToReach(moveTime)
    print(f'r = {r}')
    print('=========================')

