from typing import List
import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        # If we have x ones (x > 0) and y non-ones in the list, then those y non-ones
        # can be changed to ones in y operations, using any of the x ones.
        # Eg. [2,4,6,1,5,10,15,1,1] The non-ones will have a 1 to the left or right.
        one_count = nums.count(1)
        if one_count > 0:
            return N - one_count
        # Otherwise we find the shortest subarray that has a gcd of 1.
        MAX = 10**20
        min_len = MAX
        for i in range(N):
            g = nums[i]
            for j in range(i+1, N):
                g = math.gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
        #print(f'min_len = {min_len}')
        # If there is no such subarray then the gcd of the numbers is > 1.
        # There is no way we can convert this list to all ones. Eg. [2,4,6,8]
        if min_len == MAX:
            return -1
        # Otherwise, we will need (min_len - 1) operations to get a 1 in that subarray.
        # And then we use (N - 1) operations to convert the (N - 1) non-ones to 1.
        # So total operations = (min_len - 1) + (N - 1) = min_len + N - 2
        return min_len + N - 2

# Main section
for nums in [
               [2,6,3,4],
               [2,10,6,14],
               [6,10,15],
               [1,2,2],
               [1,1,1,1,1],
               [30, 105, 385, 1001, 2431, 4199, 7429, 12673, 20677],
               [2,3,5,7,11,13],
               [2,4,6,8,10,12,14,16],
               [2,4,6,8,10,12,14,16,7],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.minOperations(nums)
    print(f'r = {r}')
    print('=====================')




































