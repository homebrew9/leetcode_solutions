from typing import List

class Solution:
    #def heightChecker(self, heights: List[int]) -> int:
    #    ans = 0
    #    for i, j in zip(heights, sorted(heights)):
    #        if i != j:
    #            ans += 1
    #    return ans

    def heightChecker(self, heights: List[int]) -> int:
        return sum([1 for i, j in zip(heights, sorted(heights)) if i != j])

# Main section
for heights in [
                  [1,1,4,2,1,3],
                  [5,1,2,3,4],
                  [1,2,3,4,5],
               ]:
    print(f'heights = {heights}')
    sol = Solution()
    r = sol.heightChecker(heights)
    print(f'r = {r}')
    print('=============================')

