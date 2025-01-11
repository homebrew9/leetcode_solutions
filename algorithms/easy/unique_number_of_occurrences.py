from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cntr = Counter(arr)
        st = set()
        for v in cntr.values():
            if v in st:
                return False
            st.add(v)
        return True

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

