from typing import List

class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def possible(D):
            return sum(int((stations[i+1] - stations[i]) / D)
                       for i in range(len(stations) - 1)) <= k

        lo, hi = 0, 10**8
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0
            if possible(mi):
                hi = mi
            else:
                lo = mi
        return lo

# Main section
for stations, k in [
                      ([1,2,3,4,5,6,7,8,9,10], 9),
                      ([23,24,36,39,46,56,57,65,84,98], 1),
                   ]:
    print(f'stations, k = {stations}, {k}')
    sol = Solution()
    r = sol.minmaxGasDist(stations, k)
    print(f'r = {r}')
    print('=====================')





























