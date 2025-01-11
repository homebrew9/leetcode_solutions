from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            print(f'\tstones = {stones}')
            x = stones[-2]
            y = stones[-1]
            if x == y:
                del stones[-1]
                del stones[-1]
            else:
                stones[-1] = y - x
                del stones[-2]
        if len(stones) == 1:
            return stones[0]
        else:
            return 0

# Main section
for stones in [
                 [2,7,4,1,8,1],
                 [1],
                 [1,2,3,4,5,6,7,8],
                 [2,2,2,2],
                 [2,2,2,2,2],
                 [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
              ]:
    print(f'stones = {stones}')
    sol = Solution()
    r = sol.lastStoneWeight(stones)
    print(f'r = {r}')
    print('=============================')

