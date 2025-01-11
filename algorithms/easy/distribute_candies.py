from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType)//2)

# Main section
for candyType in [
                    [1,1,2,2,3,3],
                    [1,1,2,3],
                    [6,6,6,6],
                 ]:
    print(f'candyType = {candyType}')
    sol = Solution()
    r = sol.distributeCandies(candyType)
    print(f'r = {r}')
    print('==========================')

