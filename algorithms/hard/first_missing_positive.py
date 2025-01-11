from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        # The smallest missing positive number is in closed range [1, N+1].
        # All numbers > N+1, -ve nos, and 0s can be disregarded. Change them
        # to 1 if 1 is already present.
        is_one_present = False
        for n in nums:
            if n == 1:
                is_one_present = True
        if not is_one_present:
            return 1
        for i in range(N):
            if nums[i] <= 0 or nums[i] > N+1:
                nums[i] = 1
        # Now, with the exception of N, each element has its corresponding index
        # in this array. The presence of a number can be signaled by marking its
        # corresponding index. Set the number at that index as negative. For element
        # N, use the index 0.
        for i in range(N):
            ind = abs(nums[i]) % N
            if nums[ind] > 0:
                nums[ind] = -nums[ind]
        # Iterate through the array and find the first index > 0 that has a positive element.
        # Then check index 0. If that is -ve, N is present, otherwise not.
        for i in range(1, N):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return N
        else:
            return N+1

# Main section
for nums in [
               [9,8,9,11,12,13,-3,-2,-1,0,0,5,6,7,0,4,3,2,1],
               [1,2,0],
               [3,4,-1,1],
               [7,8,9,11,12],
               [5,6,7,8,0,0,-1,1,2,3,4],
               [5,6,7,8,0,0,-1,1,2,3],
               [5,6,7,8,0,0,-1,1,2],
               [5,6,7,8,0,0,-1,1],
               [5,6,7,8,0,0,-1],
               [5,6,7,8,0,0],
               [57,58,59,71,72,73,-3,-2,-1,0,0,5,6,7,0,0,3,2,1],
               [57,58,59,71,72,73,-3,-2,-1,0,0,5,6,7,0,0,3,2,1],
               [8,7,6,5,4,3,2,1],
               [23,22,21,20,19,18,17,16,0,0,0,-1,-2,15,14,13,12,11,10,9,-1,-2,-3,8,7,6,5,4,3,2,1,0,0,0],
               [9,8,9,11,12,13,-3,-2,-1,0,0,5,6,7,0,4,3,2,1],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.firstMissingPositive(nums)
    print(f'r = {r}')
    print('=================')

