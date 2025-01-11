from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        skip = False
        for i, v in enumerate(arr):
            if skip:
                skip = False
                continue
            elif v == 0:
                arr.insert(i+1, 0)
                _ = arr.pop()
                skip = True
        print(f'arr = {arr}')

# Main section
for arr in [
              [1,0,2,3,0,4,5,0],
              [1,2,3],
              [1,2,0],
              [0],
              [0,0],
              [0,0,0],
              [0,0,0,0],
              [0,0,0,0,0],
              [0,1,0,2,3],
              [0,1,2,3,4],
              [1,2,3,4,0],
              [1,2,0,4,5],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.duplicateZeros(arr)
    #print(f'r = {r}')
    print('===================')

