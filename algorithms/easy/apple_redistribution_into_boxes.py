from typing import List
from itertools import accumulate

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        arr = list(accumulate(sorted(capacity, reverse=True)))
        return sum([x < total for x in arr]) + 1

# Main section
for apple, capacity in [
                          ([1,3,2], [4,3,1,5,2]),
                          ([5,5,5], [2,4,2,7]),
                       ]:
    print(f'apple, capacity = {apple}, {capacity}')
    sol = Solution()
    r = sol.minimumBoxes(apple, capacity)
    print(f'r = {r}')
    print('==========================')









