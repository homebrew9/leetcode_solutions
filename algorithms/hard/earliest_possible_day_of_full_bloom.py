from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        res = 0
        for grow, plant in sorted(zip(growTime, plantTime)):
            res = max(res, grow) + plant
        return res

# Main section
for plantTime, growTime in [
                              ([1,4,3], [2,3,1]),
                              ([1,2,3,2], [2,1,2,1]),
                              ([1], [1]),
                           ]:
    print(f'plantTime, growTime = {plantTime}, {growTime}')
    sol = Solution()
    r = sol.earliestFullBloom(plantTime, growTime)
    print(f'r = {r}')
    print('================')

