from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def two_greatest(arr):
            first, second = 0, 0
            for item in arr:
                if item > first:
                    second = first
                    first = item
                elif item > second:
                    second = item
            return first, second

        while len(stones) > 1:
            great1, great2 = two_greatest(stones)
            #print(great1, great2)
            stones.remove(great1)
            stones.remove(great2)
            if great1 < great2:
                stones.append(great2 - great1)
            else:
                stones.append(great1 - great2)
        if len(stones) == 0:
            return 0
        else:
            return stones[0]

# Main section
for stones in [
                 [2,7,4,1,8,1],
                 [1],
                 [1,2,3,4,5,6,7,8],
                 [2,2,2,2],
                 [2,2,2,2,2],
                 [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
                 [19,5,3,2,8,16,1,20,13,14,10,30,21,6,12,11,7,29,24,23,17,27,28,15,4,25,22,26,18,9],
              ]:
    print(f'stones = {stones}')
    sol = Solution()
    r = sol.lastStoneWeight(stones)
    print(f'r = {r}')
    print('=============================')


        
