from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        N = len(flowers)
        start_times = sorted([s for s, e in flowers])
        end_times = sorted([e for s, e in flowers])
        res = list()
        for p in people:
            #print(f'p = {p}')
            left, right = 0, N - 1
            while left <= right:
                mid = (left + right)//2
                #print(left, right, mid)
                if start_times[mid] <= p:
                    left = mid + 1
                else:
                    right = mid - 1
            started_blooming = left
            #print(f'started_blooming = {started_blooming}')
            left, right = 0, N - 1
            while left <= right:
                mid = (left + right)//2
                #print(left, right, mid)
                if end_times[mid] >= p:
                    right = mid - 1
                else:
                    left = mid + 1
            stopped_blooming = left
            #print(f'stopped_blooming = {stopped_blooming}')
            res.append(started_blooming - stopped_blooming)
            #print('=====')
        return res

# Main section
for flowers, people in [
                          ([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]),
                          ([[1,10],[3,3]], [3,3,2]),
                       ]:
    print(f'flowers, people = {flowers}, {people}')
    sol = Solution()
    r = sol.fullBloomFlowers(flowers, people)
    print(f'r = {r}')
    print('===============')

