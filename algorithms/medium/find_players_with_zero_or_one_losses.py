from collections import defaultdict
from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = set()
        lossCount = defaultdict(int)
        for m in matches:
            #print(f'\t\tm, lC = {m}, {lossCount}')
            winners.add(m[0])
            losers.add(m[1])
            lossCount[m[1]] += 1
            #print(f'\t\t==> lC = {lossCount}')
        #print(f'\tlossCount = {lossCount}')
        return [sorted(list(winners - losers)), sorted([k for k, v in lossCount.items() if v == 1])]
    
# Main section
for matches in [
                  [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]],
                  [[2,3],[1,3],[5,4],[6,4]],
                  [[1,5],[2,5],[2,8],[2,9],[3,8],[4,7],[4,9],[5,7],[6,8]],
               ]:
    print(f'matches = {matches}')
    sol = Solution()
    r = sol.findWinners(matches)
    print(f'r = {r}')
    print('=====================')

