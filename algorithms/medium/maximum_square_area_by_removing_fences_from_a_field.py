from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # Add the first and last bar in both arrays.
        hFences = [1] + sorted(hFences) + [m]
        vFences = [1] + sorted(vFences) + [n]
        hLen, vLen = len(hFences), len(vFences)
        
        # Note down the current deltas in both arrays - hBars and vBars
        hset, vset = set(), set()
        for i in range(1, hLen):
            hset.add(hFences[i] - hFences[i-1])
        for i in range(1, vLen):
            vset.add(vFences[i] - vFences[i-1])
        #print(hset, vset)
                       
        # Now note down the deltas if each bar, except the ends, in hBars and vBars
        # were to be removed successively
        for i in range(0, hLen - 2):
            for j in range(i + 1, hLen - 1):
                hset.add(hFences[j+1] - hFences[i])
        for i in range(0, vLen - 2):
            for j in range(i + 1, vLen - 1):
                vset.add(vFences[j+1] - vFences[i])
        #print(hset, vset)

        # The max common delta results in the maximum square area
        # If there is no common delta, then a square area is neither existent nor
        # can be formed by removing any fence.
        if not hset.intersection(vset):
            return -1
        MOD = 10**9 + 7
        return (max(hset.intersection(vset))**2) % MOD

# Main section
for m, n, hFences, vFences in [
                                 (4, 3, [2,3], [2]),
                                 (6, 7, [2], [4]),
                                 (9, 10, [2,4,5], [3,4,6]),
                                 (10, 19, [3,4,7,9], [2,5,8,13]),
                                 (23, 31, [4,5,7,11,12,14,17], [2,6,11,12,19,23,27]),
                                 (100, 150, [6,7,9,31,45,57,79,88], [69]),
                              ]:
    print(f'm, n, hFences, vFences = {m}, {n}, {hFences}, {vFences}')
    sol = Solution()
    r = sol.maximizeSquareArea(m, n, hFences, vFences)
    print(f'r = {r}')
    print('================')

