from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Note how we can find out duplicates in a list very easily!!
        cntr = Counter(arr)
        return len(list(cntr.values())) == len(list(set(cntr.values())))

# Main section
for arr in [
              [1,2,2,1,1,3],
              [1,2],
              [-3,0,1,-3,1,1,1,-3,10,0],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.uniqueOccurrences(arr)
    print(f'r = {r}')
    print('===========================')

