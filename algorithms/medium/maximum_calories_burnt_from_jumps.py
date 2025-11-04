from typing import List

class Solution:
    def maxCaloriesBurnt(self, heights: List[int]) -> int:
        N = len(heights)
        heights.sort(reverse=True)
        res = 0
        prev = 0
        left, right = 0, N - 1
        while left < right:
            res += (heights[left] - prev)**2
            res += (heights[right] - heights[left])**2
            prev = heights[right]
            left += 1
            right -= 1
        if left == right:
            res += (heights[left] - prev)**2
        return res

# Main section
for heights in [
                  [1,7,9],
                  [5,2,4],
                  [3,3],
               ]:
    print(f'heights = {heights}')
    sol = Solution()
    r = sol.maxCaloriesBurnt(heights)
    print(f'r = {r}')
    print('=====================')




















