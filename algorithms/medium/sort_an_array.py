from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(arr, low, high):
            if low < high:
                mid = (low + high) // 2
                mergesort(arr, low, mid)
                mergesort(arr, mid+1, high)
                merge(arr, low, mid, mid+1, high)
            return arr

        def merge(arr, p, q, r, s):
            #print(f'arr, (p, q), (r, s) = {arr}, ({p}, {q}), ({r}, {s})')
            arr1 = arr[p:q+1]
            arr2 = arr[r:s+1]
            #print(f'\tarr1 = {arr1}, arr2 = {arr2}')
            mrg = mergeLists(arr1, arr2)
            #print(f'\tmrg = {mrg}')
            j = p
            for i in range(len(mrg)):
                arr[j] = mrg[i]
                j += 1
            #print(f'\tarr = {arr}')

        def mergeLists(arr1, arr2):
            arr = []
            i, j = 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    arr += [arr1[i]]
                    i += 1
                elif arr2[j] < arr1[i]:
                    arr += [arr2[j]]
                    j += 1
                elif arr1[i] == arr2[j]:
                    arr += [arr1[i], arr2[j]]
                    i += 1
                    j += 1
            while i < len(arr1):
                arr += [arr1[i]]
                i += 1
            while j < len(arr2):
                arr += [arr2[j]]
                j += 1
            return arr

        return mergesort(nums, 0, len(nums)-1)

# Main section
for nums in [
               [5,7,3,1,9,8,2]
               #[5,2,3,1],
               #[5,1,1,2,0,0],
               #[5,9,3,0,1,8],
               #[0,1,2,3,4,5],
               #[-5,-4,0,-9,4,5,3,1],
               #[9,8,4,7,2,0,1,-8,4,9,0,5,3,3,5],
               #[-1,-2,-3,-4,-5,-6,-7,-8],
               #[5,4,3,2,1,0],
               #[9],
               #[9,8],
               #[],
               #[9,9],
               #[9,-9,0],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.sortArray(nums)
    print(f'r = {r}')
    print('===================')

