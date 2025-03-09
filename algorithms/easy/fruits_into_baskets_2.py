from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        N = len(fruits)
        res = 0
        for i in range(N):
            f = fruits[i]
            idx = None
            for j in range(len(baskets)):
                if f <= baskets[j]:
                    idx = j
                    break
            if idx is None:
                res += 1
            else:
                del baskets[idx]
        return res

# Main section
for fruits, baskets in [
                          ([4,2,5], [3,5,4]),
                          ([3,6,1], [6,4,7]),
                       ]:
    print(f'fruits, baskets = {fruits}, {baskets}')
    sol = Solution()
    r = sol.numOfUnplacedFruits(fruits, baskets)
    print(f'r = {r}')
    print('=========================')

