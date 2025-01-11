#
# The first algorithm uses O(N) time complexity. But it has to be solved in
# O(log-n) time complexity.
from typing import List
class Solution:
    #def peakIndexInMountainArray(self, arr: List[int]) -> int:
    #    for i in range(1, len(arr)-1):
    #        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
    #            return i

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1
        print(f'\tlow, high = {low}, {high}')
        while low <= high:
            mid = (low + high) // 2
            if arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] < arr[mid] < arr[mid+1]:
                low = mid
            else:
                high = mid
            print(f'\t\tlow, mid, high = {low}, {mid}, {high}')
        print(f'\tlow, mid, high = {low}, {mid}, {high}')

# Main section
for arr in [
              [0,1,0],
              [0,2,1,0],
              [0,10,5,2],
              [1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1],
              [0,3,8,19,37,17],
              [0,13,8,1,0],
              [0,13,8,1,0,-1],
              [-1,0,13,8,1,0,-1],
              [-1,0,1,8,9,10,-1],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.peakIndexInMountainArray(arr)
    print(f'r = {r}')
    print('===================')

