from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bsearch(arr, t):
            #print(f'\tarr, t = {arr}, {t}')
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                #print(f'\t\tleft, mid, right = {left}, {mid}, {right}')
                if arr[mid] == target:
                    return True
                elif target > arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        if target < matrix[0][0] or target > matrix[rows-1][cols-1]:
            return False
        for row in range(rows):
            if matrix[row][0] <= target <= matrix[row][cols-1]:
                if bsearch(matrix[row], target):
                    return True
        return False

# Main section
for matrix, target in [
                         ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3),
                         ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13),
                         ([[1]], 1),
                         ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 34),
                         ([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 70),
                      ]:
    print(f'matrix, target = {matrix}, {target}')
    sol = Solution()
    r = sol.searchMatrix(matrix, target)
    print(f'r = {r}')
    print('================')


