from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums, low, high):
            if low < high:
                mid = (low + high) // 2
                mergeSort(nums, low, mid)
                mergeSort(nums, mid+1, high)
                merge(nums, low, mid, high)
            return nums

        def merge(nums, low, mid, high):
            #print(f'\tnums, low, mid, high = {nums}, {low}, {mid}, {high}')
            # temp array to store sorted elements
            arr = []
            arr1 = nums[low:mid+1]
            arr2 = nums[mid+1:high+1]
            i, j = 0, 0
            while True:
                if arr1[i] == arr2[j]:
                    arr += [arr1[i]]
                    arr += [arr2[j]]
                    i += 1
                    j += 1
                elif arr1[i] < arr2[j]:
                    arr += [arr1[i]]
                    i += 1
                elif arr2[j] < arr1[i]:
                    arr += [arr2[j]]
                    j += 1
                if i >= len(arr1):
                    break
                if j >= len(arr2):
                    break
            while i < len(arr1):
                arr += [arr1[i]]
                i += 1
            while j < len(arr2):
                arr += [arr2[j]]
                j += 1
            # Copy the elements of temp array arr back to nums
            for k in range(len(arr)):
                nums[low+k] = arr[k]
            #print(f'\tnums = {nums}')
            #print('=========')

        mergeSort(nums, 0, len(nums)-1)
        return nums

# Main section
for nums in [
               [5,7,3,1,9,8,2],
               [5,2,3,1],
               [5,1,1,2,0,0],
               [5,9,3,0,1,8],
               [0,1,2,3,4,5],
               [-5,-4,0,-9,4,5,3,1],
               [9,8,4,7,2,0,1,-8,4,9,0,5,3,3,5],
               [-1,-2,-3,-4,-5,-6,-7,-8],
               [5,4,3,2,1,0],
               [9],
               [9,8],
               [],
               [9,9],
               [9,-9,0],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.sortArray(nums)
    print(f'r    = {r}')
    print('===================')


