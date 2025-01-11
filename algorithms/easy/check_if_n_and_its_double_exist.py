from typing import List
from collections import Counter

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        ct = Counter(arr)
        st = set(arr)
        for i in st:
            #print(f'i = {i}')
            if i == 0:
                #print('in 1st if')
                if ct[i] > 1:
                    return True
            else:
                #print('in else')
                if 2*i in st:
                    return True
        return False

# Main section
for arr in [
              [10,2,5,3],
              [3,1,7,11],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.checkIfExist(arr)
    print(f'r = {r}')
    print('===================')

