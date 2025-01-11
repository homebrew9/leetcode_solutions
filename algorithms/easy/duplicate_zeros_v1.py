#
# Dumping elements in new array does not work.
# Trying the idea from Leetcode Solution.
# Does not work for some cases!! The last test case fails!
#
from typing import List

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        size = len(arr)
        zero_count = 0
        left = 0
        right = size - 1
        while True:
            if arr[left] == 0:
                zero_count += 1
                right -= 1
            left += 1
            if left >= right:
                break

        if zero_count > 0 and zero_count < size:
            arr[-zero_count:] = [None]*zero_count
            left = size - zero_count - 1
            right = size - 1
            while True:
                if arr[left] != 0:
                    arr[right] = arr[left]
                    right -= 1
                    left -= 1
                else:
                    arr[right] = 0
                    right -= 1
                    arr[right] = 0
                    right -= 1
                    left -= 1
                if right <= left:
                    break
        print(f'arr = {arr}')

# Main section
for arr in [
              #[1,0,2,3,0,4,5,0],
              #[1,2,3],
              #[1,2,0],
              #[0],
              #[9],
              #[0,0],
              #[0,0,0],
              #[0,0,0,0],
              #[0,0,0,0,0],
              #[0,1,0,2,3],
              #[0,1,2,3,4],
              #[1,2,3,4,0],
              #[1,2,0,4,5],
              #[0,1,7,6,0,2,0,7],
              #[0,1,7,6,9,2,7,0],
              #[9,9,9,4,8,0,0,3,7,2,0,0,0,0,9,1,0,0,1,1,0,5,6,3,1,6,0,0,2,3,4,7,0,3,9,3,6,5,8,9,1,1,3,2,0,0,7,3,3,0,5,7,0,8,1,9,6,3,0,8,8,8,8,0,0,5,0,0,0,3,7,7,7,7,5,1,0,0,8,0,0],
              [9,9,9,4,8,0,0,3,7,2,0,0,0,0,9,1,0,0],
           ]:
    print(f'arr = {arr}')
    sol = Solution()
    r = sol.duplicateZeros(arr)
    #print(f'r = {r}')
    print('===================')

