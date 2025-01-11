from typing import List

class Solution:
    # Incorrect logic! Does not work for last test case!
    #def maxDistance(self, colors: List[int]) -> int:
    #    left, right = 0, len(colors) - 1
    #    while left < right:
    #        if colors[left] != colors[right]:
    #            return abs(right - left)
    #        right -= 1

    def maxDistance(self, colors: List[int]) -> int:
        max_dist = 0
        for i in range(0, len(colors) - 1):
            for j in range(i+1, len(colors)):
                if colors[i] != colors[j] and abs(i-j) > max_dist:
                    max_dist = abs(i-j)
        return max_dist

# Main section
for colors in [
                 [1,1,1,6,1,1,1],
                 [1,8,3,8,3],
                 [0,1],
                 [1,2,3,4,5,6,5,4,3,2,1],
                 [1,2,3,4,5,6,7,8],
                 [8,7,6,5,4,3,2,1],
                 [1,1,1,1,1,2,3,1,1,1,1],
                 [4,4,4,11,4,4,11,4,4,4,4,4],
              ]:
    print(f'colors = {colors}')
    sol = Solution()
    r = sol.maxDistance(colors)
    print(f'r = {r}')
    print('===========================')

