from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        slope = None
        i = 1
        while i < len(arr):
            if i == 1:
                if arr[i] <= arr[i-1]:
                    return False
                slope = 'up'
            elif slope == 'up':
                if arr[i] < arr[i-1]:
                    slope = 'down'
                elif arr[i] == arr[i-1]:
                    return False
            elif slope == 'down':
                if arr[i] >= arr[i-1]:
                    return False
            i += 1
        if slope == 'up':
            return False
        return True

# Main section
for arr in [
              [2,1],
              [3,5,5],
              [0,3,2,1],
              [0,2,3,4,5,2,1,0],
              [5,3,1],
              [3,5,7],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.validMountainArray(arr)
    print(f'r = {r}')
    print('=============================')

