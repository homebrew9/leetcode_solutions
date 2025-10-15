from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # Intuition: Determine strictly increasing subarray as long as possible.
        # prevLen is the length of the previous strictly increasing subarray.
        # curLen is the length of the current strictly increasing subarray.
        # Option 1: previous and current lengths are both >= k
        # Option 2: current length >= 2k i.e. it has two strictly increasing subarrays
        # in it, each of which is of length >= k.
        # TC = O(N), SC = O(1)
        N = len(nums)
        prevLen, curLen = 0, 1
        for i in range(1, N):
            if nums[i] > nums[i-1]:
                curLen += 1
            else:
                prevLen, curLen = curLen, 1
            if (curLen >= k and prevLen >= k) or curLen == 2*k:
                return True
        return False

# Main section
for nums, k in [
                  ([2,5,7,8,9,2,3,4,3,1], 3),
                  ([1,2,3,4,4,4,4,5,6,7], 5),
               ]:
    print(f'nums, k = {nums}, {k}')
    sol = Solution()
    r = sol.hasIncreasingSubarrays(nums, k)
    print(f'r = {r}')
    print('=====================')

