#
# Solution by user: "hiepit"
# Ref: https://leetcode.com/problems/duplicate-zeros/discuss/898225/Python-2-solutions-Easy-to-understand-Time-O(N)-Space-O(1)
#
from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        org = arr[:] # Note that this does a deep copy of arr to org!
        i = 0
        j = 0
        size = len(arr)
        while j < size:
            arr[j] = org[i]
            j += 1
            if org[i] == 0:
                # Copy twice
                if j < size:
                    arr[j] = org[i]
                    j += 1
            i += 1

        print(f'arr = {arr}')

# Main section
for arr in [
              [1,2,0,3,4],
              [1,0,2,3,0,4,5,0],
              [1,0,2,3,0,0,5,0],
              [1,2,3],
              [1,2,0],
              [0],
              [9],
              [0,0],
              [0,0,0],
              [0,0,0,0],
              [0,0,0,0,0],
              [0,1,0,2,3],
              [0,1,2,3,4],
              [1,2,3,4,0],
              [1,2,0,4,5],
              [0,1,7,6,0,2,0,7],
              [0,1,7,6,9,2,7,0],
              [9,9,9,4,8,0,0,3,7,2,0,0,0,0,9,1,0,0,1,1,0,5,6,3,1,6,0,0,2,3,4,7,0,3,9,3,6,5,8,9,1,1,3,2,0,0,7,3,3,0,5,7,0,8,1,9,6,3,0,8,8,8,8,0,0,5,0,0,0,3,7,7,7,7,5,1,0,0,8,0,0],
              [9,9,9,4,8,0,0,3,7,2,0,0,0,0,9,1,0,0],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.duplicateZeros(arr)
    #print(f'r = {r}')
    print('===================')



