from typing import List
from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        best = 0
        count = Counter()
        left = 0
        for right in range(N):
            #print(f'\tleft, right, count = {left}, {right}, {count}')
            count[fruits[right]] += 1
            while len(count) >= 3:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1
            best = max(best, right-left+1)
        return best

# Main section
for fruits in [
                 [0,0,0,1,1,1,1,2,2,3,3,3,3,3,3,4,4,4,4],
                 [1,2,1],
                 [0,1,2,2],
                 [1,2,3,2,2],
                 [1,2,2,1,3,3,4,3,4,6,7],
                 [1,2,2,1,3,3,4,3,4,5,5,5,5,4,4,6],
              ]:
    print(f'fruits = {fruits}')
    sol = Solution()
    r = sol.totalFruit(fruits)
    print(f'r = {r}')
    print('================')

