from typing import List

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()
        for i in range(len(nums)-1):
            curr_sum = nums[i] + nums[i+1]
            if curr_sum in sums:
                return True
            else:
                sums.add(curr_sum)
        return False

# Main section
for nums in [
               [4,2,4],
               [1,2,3,4,5],
               [0,0,0],
            ]:
    print(f'nums = {nums}')
    sol = Solution()
    r = sol.findSubarrays(nums)
    print(f'r = {r}')
    print('=====================')

