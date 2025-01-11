from typing import List

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        # The only case where we won't be able to cancel out two (therefore, equal)
        # values is if some value occurs more than half the time,
        # e.g. [1, 1, 2, 5, 5, 5, 5, 5, 5, 6]. In this case, at some point the
        # left pointer and right pointer will hit this most common value. In our
        # example, it would first happen at i=3 and j=8, where nums[3]=nums[8]=5.
        # So we simply move the pointers by one. We keep moving it by one as long
        # as the pointers hit the same value.
        # In all other cases, the left and right pointer will point to two different
        # values, so we cancel them out
        N = len(nums)
        i = 0
        j = (N + 1)//2
        #j = N//2
        print(f'\tj = {j}')
        used = 0
        while j < N:
            print(f'\t\ti, j = ({i}, {j}) ; nums[i], nums[j] = ({nums[i]}, {nums[j]}) ; used = {used}')
            if nums[i] < nums[j]:
                i += 1
                used += 1
            j += 1
        print(f'\tused = {used}')
        return N - 2*used

# Main section
for nums in [
               [1,3,4,9],
               [2,3,6,9],
               [1,1,2],
               [2,2,2,2,3,3,3,3,5,6,7,7],
               [2,2,3,5,6,7,7],
               [2,2,2,5,6,7,7],
               [2,2,3,3,5,6,7,7],
               [2,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5,5,5,5,7,7,7,7,7,9,9,9,11,11,11],
               [2,2,3,5,6,7,7],
               [2,2,2,5,6,7,7],
               [2,2,2,2,2,2],
               [2,2,2,2,2,3],
               [2,2,2,2,3,3],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minLengthAfterRemovals(nums)
    print(f'r = {r}')
    print('====================')

