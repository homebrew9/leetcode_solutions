from typing import List

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_dist = 10**20
        for i, n in enumerate(nums):
            if n == target:
                min_dist = min(min_dist, abs(i - start))
        return min_dist

# Main section
for nums, target, start in [
                              ([1,2,3,4,5], 5, 3),
                              ([1], 1, 0),
                              ([1,1,1,1,1,1,1,1,1,1], 1, 0),
                           ]:
    print(f'nums, target, start = {nums}, {target}, {start}')
    sol = Solution()
    r = sol.getMinDistance(nums, target, start)
    print(f'r = {r}')
    print('==================================')




