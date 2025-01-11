#
# See also: https://www.youtube.com/watch?v=Fqf1tOm1cEM
# Exponent => Contiguous subarray sum
#
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # The dictionary "hsh" has the following components:
        # key = (running sum up to index i) % k
        # value = i (the index). Let's say nums = [23,2,6,4,7] and k = 12
        # i = 0; run_sum = 23; r = 11; hsh = {11: 0}
        # i = 1; run_sum = 25; r =  1; hsh = {11: 0, 1: 1}
        # i = 2; run_sum = 31; r =  7; hsh = {11: 0, 1: 1, 7: 2}
        # i = 3; run_sum = 35; r = 11; hsh = {11: 0, 1: 1, 7: 2}; key = 11, value = 3
        # Now, the key 11 already exists in hsh and has the value 0. This means that
        # at index 0, the (running sum up to index 0) % 12 = 11. And now we see that
        # (running sum up to index 3) % 12 = 11. Specifically:
        # For index = 0: (23) % 12 = 11
        # For index = 3: (23 + 2 + 6 + 4) % 12 = 11. This means that the diff of
        # run_sum values is a multiple of 12 => (23+2+6+4) - (23) = 12.
        # We simply check the diff of values, and if that is >= 2, then we return True.
        hsh = {0: -1}
        N = len(nums)
        run_sum = 0
        for i in range(0, N):
            #print(i, nums[i], run_sum, hsh)
            run_sum += nums[i]
            rem = run_sum % k
            if not rem in hsh:
                hsh[rem] = i
            else:
                if i - hsh[rem] >= 2:
                    return True
        return False

# Main section
for nums, k in [
                  ([23,2,4,6,7], 6),
                  ([23,2,6,4,7], 13),
                  ([5,0,0,], 3),
                  ([1,1,1,1,1], 5),
                  ([1,2,3,4,5], 15),
                  ([1,2,3,4,5], 16),
                  ([2,4,3], 6),
                  ([23,2,4,6,6], 7),
                  ([23,2,4,6,7], 6),
                  ([23,2,6,4,7], 6),
                  ([23,2,6,4,7], 13),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.checkSubarraySum(nums, k)
    print(f'r = {r}')
    print('=====================')


