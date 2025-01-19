from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # This is the Narayan Pandita Algorithm in Knuth's TAOCP Volume 4A
        N = len(nums)
        # Find the rightmost i such that A[i] < A[i+1] ......(1)
        i = None
        for ind in range(0, N-1):
            if nums[ind] < nums[ind+1]:
                i = ind
        # If no such i is found, then the array is already at its last permutation, and
        # it is reverse-sorted. The next permutation is the sorted array, as per the problem.
        # So we simply run a two-pointer loop and reverse the array in place
        if i is None:
            left, right = 0, N - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            print(f'nums = {nums}')
            return
        # Find the rightmost j, where j > i, such that A[j] > A[i]  .......(2)
        for ind in range(i+1, N):
            if nums[ind] > nums[i]:
                j = ind
        # Swap A[i] and A[j]  .........(3)
        nums[i], nums[j] = nums[j], nums[i]
        # Sort the subarray A[i+1:] (here i is the original i from step 1)
        # Since this is in-place, we can use selection sort on the array chunk A[i+1:]
        for p in range(i+1, N):
            min_ind, min_val = None, float('inf')
            for q in range(p, N):
                if nums[q] < min_val:
                    min_ind, min_val = q, nums[q]
            nums[p], nums[min_ind] = nums[min_ind], nums[p]
        print(f'nums = {nums}')

# Main section
for nums in [
               [1,2,3],
               [3,2,1],
               [1,1,5],
               [1,2,3,4,3,2,1],
               [1,4,1,8,3,1,1],
               [5,5,7,5,6,7,0,9,3,6,6,4,0,6,3,9,8,7,6,5],
               [5,1,2,1,5,4,0,3,5,1,0,9,0,2,4,8,3,1,9,6,3,9,0,7,5,7,6,6,7,8,6,4,4,0,3,7,2,6,2,0,7,6,6,2,4,8,4,9,7,7],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.nextPermutation(nums)
    print(f'r = {r}')
    print('=====================')


